import flet as ft
import time
# from pages.login import LoginPage
from app.backend.router import get_page

class Content(ft.Container):
    def __init__(
            self,
            init_page: str = "home"
        ):
        super().__init__()
        self.expand = True

        self.init_page = init_page

        # Contenuto iniziale
        self.current_control = None

        self.content = ft.Column(
            controls=[self.current_control],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            scroll=ft.ScrollMode.AUTO
        )

        # Animazione fade
        self.animate_opacity = ft.Animation(400, ft.AnimationCurve.EASE_IN_OUT)
        self.opacity = 1

        self.controls = self.content

    def did_mount(self):
        self.set_content(self.init_page)

    def fade_out_in(self, new_control: ft.Control):
        """Esegue la dissolvenza e sostituisce il contenuto."""
        # 1️⃣ Fade out
        self.opacity = 0
        self.update()
        time.sleep(0.3)  # breve pausa per l'animazione

        # 2️⃣ Aggiorna contenuto (sostituisce tutto, non solo testo)
        self.content.controls.clear()
        self.content.controls.append(new_control)
        self.current_control = new_control

        # 3️⃣ Fade in
        self.opacity = 1
        self.update()

    def set_content(self, page_name: str):
        """Cambia il contenuto in base al nome pagina."""
        new_control = get_page(page_name)
        self.fade_out_in(new_control)
