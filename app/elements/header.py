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

        self.title = ft.Text("Studio legale Repetto e DeBianchi", weight=ft.FontWeight.BOLD, animate_size=200)

        self.menu_inline = ft.Row(
            visible=True,
            controls=[
                ft.TextButton("Home", style=ft.ButtonStyle(color=default.COLOR_2) ,on_click=lambda _: self.menu_item_clicked("Home")),
                ft.TextButton("Chi Siamo", style=ft.ButtonStyle(color=default.COLOR_2) ,on_click=lambda _: self.menu_item_clicked("Chi Siamo")),
                ft.TextButton("Contatti", style=ft.ButtonStyle(color=default.COLOR_2) ,on_click=lambda _: self.menu_item_clicked("Contatti"))
            ]
        )

        self.menu_dropdown = ft.PopupMenuButton(
            visible=False,
            popup_animation_style=ft.AnimationStyle(duration=300, curve=ft.AnimationCurve.EASE_OUT),
            animate_opacity=300,
            items=[
                ft.PopupMenuItem("Home"),
                ft.PopupMenuItem("Chi Siamo"),
                ft.PopupMenuItem("Contatti"),
            ],
            on_select=lambda e: self.menu_item_clicked(str(e.control.value).lower())
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
        self.title.size = default.TEXT_MEDIUM_SIZE
        self.header.content.height = 70

        self.update()

    # Vista desktop
    def set_default_view(self):
        print("Switching to DESKTOP view")
        # properties specifiche per desktop
        self.menu_inline.visible = True
        self.menu_dropdown.visible = False

        # EFFECTS
        self.title.size = default.TEXT_LARGE_SIZE
        self.header.content.height = 80

        self.update()
    
    ## FUNCTIONS