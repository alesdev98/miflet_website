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

        self.menu_inline = ft.Row(
            animate_opacity=300,
            visible=True,
            controls=[
                ft.TextButton("Home", on_click=lambda _: self.menu_item_clicked("Home")),
                ft.TextButton("Chi Siamo", on_click=lambda _: self.menu_item_clicked("Chi Siamo")),
                ft.TextButton("Contatti", on_click=lambda _: self.menu_item_clicked("Contatti"))
            ]
        )

        self.menu_dropdown = ft.Dropdown(
            animate_opacity=300,
            on_select=lambda e: self.menu_item_clicked(e.control.value),
            visible=False,
            color=default.COLOR_2,
            options=[
                ft.dropdown.Option("Home"),
                ft.dropdown.Option("Chi Siamo"),
                ft.dropdown.Option("Contatti")
            ]
        )

        # Elements
        self.header = ft.Container(
            animate=ft.Animation(220, ft.AnimationCurve.EASE_OUT),
            bgcolor=default.COLOR_1,
            content=ft.Row(
                height=80,
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    ft.Text("Studio legale Repetto e DeBianchi", weight=ft.FontWeight.BOLD, animate_size=200),
                    self.menu_inline,
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

        self.media.on('mobile', self.set_mobile_view)
        self.media.on('default', self.set_default_view)

        self.update()

    # Vista mobile
    def set_mobile_view(self):
        print("Switching to MOBILE view")
        # properties specifiche per mobile
        self.menu_inline.visible = False
        self.menu_dropdown.visible = True

        # EFFECTS
        self.header.content.controls[0].size = default.TEXT_MEDIUM_SIZE
        self.header.height = 70
        self.menu_inline.opacity = 0
        self.menu_dropdown.opacity = 1

        self.update()

    # Vista desktop
    def set_default_view(self):
        print("Switching to DESKTOP view")
        # properties specifiche per desktop
        self.menu_inline.visible = True
        self.menu_dropdown.visible = False

        # EFFECTS
        self.header.content.controls[0].size = default.TEXT_LARGE_SIZE
        self.header.height = 80
        self.menu_inline.opacity = 1
        self.menu_dropdown.opacity = 0

        self.update()
    
    ## FUNCTIONS