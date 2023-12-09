from engine.component.builtins import ColliderComponent
from engine.draw import Draw
from engine.game_object import GameObject
from engine.input import Keys
from engine.picocore import PicoCore
from _platform import Platform


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
