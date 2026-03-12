import flet as ft
import app.elements.default as default

from app.media.responsive import MediaQuery

img_path = "static"

class Header(ft.Container):

    def __init__(
            self, 
            media: MediaQuery = None,
            toggle_theme_mode=None,
            on_menu_select=None
        ):
        super().__init__()

        # Stato interno
        self.media = media  # oggetto MediaQuery per gestire la responsività
        self.toggle_theme_mode = toggle_theme_mode  # callback per il toggle tema
        self.on_menu_select = on_menu_select  # callback per comunicare col Content

        # Elementi UI
        LINKS = ["Home", "Chi Siamo", "Aree di Attività", "Contatti"]

        self.title = ft.Text("Studio legale Repetto e DeBianchi", size=default.TEXT_XXL_SIZE, weight=ft.FontWeight.BOLD, animate_size=200)

        self.icon = ft.Image(src=f"{img_path}/logo.png", color=default.COLOR_2, visible=False)

        self.theme_toggle = ft.IconButton(
            icon=ft.Icons.DARK_MODE,
            on_click=lambda _: self.toggle_theme_mode()
        )

        # MENU
        self.menu_inline = ft.Row(
            visible=True,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.TextButton(
                    str(link), 
                    style=ft.ButtonStyle(text_style=ft.TextStyle(size=default.TEXT_L_SIZE, color=default.COLOR_2)),
                    on_click=lambda _: self.menu_item_clicked(str(link).lower())
                ) for link in LINKS
            ] 
        )

        self.menu_dropdown = ft.PopupMenuButton(
            visible=False,
            popup_animation_style=ft.AnimationStyle(duration=300, curve=ft.AnimationCurve.EASE_OUT),
            animate_opacity=300,
            items=[
                ft.PopupMenuItem(f"{link}", on_click=lambda _, l=link: self.menu_item_clicked(l.lower()))
                for link in LINKS
            ]
        )

        # Elements
        self.header = ft.Container(
            animate=ft.Animation(220, ft.AnimationCurve.EASE_OUT),
            bgcolor=default.COLOR_1,
            content=ft.Row(
                height=80,
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    self.title,
                    self.icon,
                    self.menu_inline,
                    self.theme_toggle,
                    self.menu_dropdown
                ]
            )
        )

        self.content = ft.Stack(
            controls=[
                self.header
            ],
            expand=True
        )

        self.controls = [
            self.content
        ]

    def menu_item_clicked(self, item_name: str):
        print(f"Menu item clicked: {item_name}")
        if self.on_menu_select:
            self.on_menu_select(item_name)  # chiama la callback passata da main()
    
    def did_mount(self):

        async def load_session():
            try:
                token = await ft.SharedPreferences().get(key="session_token")
            except Exception as e:
                print(f"Errore nel recupero del token: {e}")
            self.update()
        self.page.run_task(load_session)

        if self.page.platform in (ft.PagePlatform.ANDROID, ft.PagePlatform.IOS):
            self.set_mobile_view()
        else:
            self.media.on('mobile', self.set_mobile_view)
            self.media.on('default', self.set_default_view)

        self.theme_toggle.icon = ft.Icons.DARK_MODE if self.page.theme_mode == ft.ThemeMode.LIGHT else ft.Icons.LIGHT_MODE

        self.update()

    # Vista mobile
    def set_mobile_view(self):
        print("Switching to MOBILE view")
        # properties specifiche per mobile
        self.menu_inline.visible = False
        self.menu_dropdown.visible = True
        
        # EFFECTS
        # self.title.size = default.TEXT_L_SIZE
        self.title.visible = False
        self.icon.visible = True
        self.header.content.height = 70

        self.update()

    # Vista desktop
    def set_default_view(self):
        print("Switching to DESKTOP view")
        # properties specifiche per desktop
        self.menu_inline.visible = True
        self.menu_dropdown.visible = False

        # EFFECTS
        self.title.size = default.TEXT_XXL_SIZE
        self.title.visible = True
        self.icon.visible = False
        self.header.content.height = 80

        self.update()
    
    ## MAIN CALLBACKS
    def theme_toggle_icon(self, icon: ft.Icons):
        self.theme_toggle.icon = icon
        self.update()
    
