from engine.draw import Draw
from engine.game_object import GameObject


class Fruit(GameObject):
    def on_start(self):
        pass

    def on_update(self, delta_time):
        pass

    def __init__(self, core, x, y, height=20, width=20, debug=False):
        super().__init__(core, x, y, width, height, debug=debug)

    def on_draw(self):
        Draw.change_color("#FFFF00")
        Draw.rect(20, -10, 30, 30)
        Draw.rect(12, 10, 5, 5, True)
