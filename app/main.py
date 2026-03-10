import flet as ft

def main(page: ft.Page):
    page.title = "My Flet Website"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Text("Il mio sito Flet è online 🚀", size=40),
        ft.ElevatedButton("Click")
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)