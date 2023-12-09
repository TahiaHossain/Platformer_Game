from engine.draw import Draw
from engine.game_object import GameObject


class Enemy(GameObject):

    def on_start(self):
        pass

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        Draw.change_color("#FF0000")
        Draw.rect(0, 0, 50, 50)
