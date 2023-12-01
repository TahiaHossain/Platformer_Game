from engine.draw import Draw
from engine.game_object import GameObject


class Enemy(GameObject):

    def on_start(self):
        pass

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        Draw.change_color("#FF0000")
        Draw.circle(10, 0, 0)
