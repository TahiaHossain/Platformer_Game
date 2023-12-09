from platform import Platform
from engine.draw import Draw


class Floor(Platform):
    def __init__(self, core, x, y):
        super().__init__(core, x, y)
        self.width = core.width
        self.height = 100

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        Draw.change_color("#FFFFFF")
        Draw.rect(0, 0, self.width, self.height)
