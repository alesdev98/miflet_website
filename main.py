import flet as ft

from app.media.responsive import MediaQuery

from app.elements.header import Header
from app.elements.content import Content

async def main(page: ft.Page):
    # CALLBACKS
    def theme_mode_toggle():
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        page.update()

    def on_menu_select(page_name: str):
        content.set_content(page_name)

    # Recupera il token salvato
    try:
        session_token = await ft.SharedPreferences().get(key="session_token")
        # if not(session_token and user_active_session(session_token)):
        if not(session_token):
            print("Nessun token di sessione valido trovato.")
            await ft.SharedPreferences().remove(key="session_token")
    except Exception as e:
        print(f"Errore nel recupero del token di sessione: {e}")
        await ft.SharedPreferences().remove(key="session_token")

    media = MediaQuery(page)
    media.register("mobile", min_width=0, max_width=600)
    media.register("default", min_width=601, max_width=2000)
    
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK

    # ELEMENTS INIT
    header = Header(
        media=media,
        toggle_theme_mode=theme_mode_toggle,
        on_menu_select=on_menu_select
    )
    content = Content()

    # PAGE
    page.add(header)
    page.add(content)

ft.run(
    main=main,
    assets_dir="assets",
    port=8000
)