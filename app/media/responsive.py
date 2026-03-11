import flet


class MediaQueryManager:
    def __init__(self, page: flet.Page):
        self.page = page
        self.breakpoints = {}
        self.listeners = {}
        self.current_breakpoint = None

    def _detect(self, width):
        if not width:
            return

        for name, (min_w, max_w) in self.breakpoints.items():
            if min_w <= width <= max_w:
                if self.current_breakpoint != name:
                    self.current_breakpoint = name

                    for callback in self.listeners.get(name, []):
                        callback()

    def handle_resize(self, e: flet.ControlEvent):
        width = e.page.width
        self._detect(width)


class MediaQuery:
    def __init__(self, page: flet.Page):
        if not hasattr(page, "_media_query"):
            page._media_query = MediaQueryManager(page)

            # collega resize una sola volta
            page.on_resize = page._media_query.handle_resize

        self.page = page

    def register(self, point, min_width, max_width):
        self.page._media_query.breakpoints[point] = (min_width, max_width)

        if point not in self.page._media_query.listeners:
            self.page._media_query.listeners[point] = []

    def on(self, point, callback):
        if point not in self.page._media_query.listeners:
            self.page._media_query.listeners[point] = []

        self.page._media_query.listeners[point].append(callback)

        # trigger iniziale DOPO il mount della pagina
        width = self.page.width
        self.page._media_query._detect(width)

    def off(self, point, callback):
        if point in self.page._media_query.listeners:
            if callback in self.page._media_query.listeners[point]:
                self.page._media_query.listeners[point].remove(callback)