from engine.draw import Draw
from engine.game_object import UiObject


class Label(UiObject):

    def __init__(self, core, text: str, x, y, size=10, spacing=5, alignment="center", color="#FFFFFF"):
        self.width = (len(text) * size) + ((len(text) - 1) * spacing)
        super().__init__(core, x, y, width=self.width, height=size)
        self.text = text
        self.color = color
        self.size = 10
        self.spacing = 5
        self.draw_x = 0
        self.draw_y = 0

        if alignment == "center":
            self.draw_x -= self.width / 2
        elif alignment == "left":
            self.draw_x -= self.width
        elif alignment == "right":
            self.draw_x = 0

    def on_start(self):
        pass

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        Draw.change_color(self.color)
        Draw.text(self.text, self.draw_x, 0, size=self.size, spacing=self.spacing)
