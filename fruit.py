from engine.draw import Draw
from engine.game_object import GameObject


class Fruit(GameObject):

    def __init__(self, core, x, y, width=30, height=30, debug=False):
        super().__init__(core, x, y, width, height, debug=debug)

    def on_start(self):
        pass

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        Draw.change_color("#FFFF00")
        Draw.rect(0, 0, self.width, self.height)
        Draw.rect(-5, 5, 5, 5, True)
