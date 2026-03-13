# backend/router.py
import flet as ft

from app.pages.home import *

def get_page(page_name: str, on_user_change_token=None) -> ft.Control:
    """Restituisce un controllo Flet in base al nome della pagina."""
    page_name = page_name.lower()
    print(f"➡️ Routing verso: {page_name}")

    match page_name:
        case "home":
            return Home()
        case "about":
            return ft.Text("ℹ️ Informazioni su StampaCheTiPassa", size=20)
        case "contact":
            return ft.Text("📞 Contattaci!", size=20)
        case "admin_dashboard":
            return ft.Text("📊 Dashboard Admin", size=20)
        case _:
            return ft.Text(f"❌ Pagina non trovata: {page_name}", size=20)
