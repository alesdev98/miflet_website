import flet as ft

class Home(ft.Container):
    def __init__(
            self
        ):
        super().__init__()

        # Stato interno
        
        self.content = ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            controls=[ft.Text("🏠 Benvenuto nella 2!", size=20)]
        )
    
    def did_mount(self):
        pass

        