from engine.button import Button
from engine.draw import Draw
from engine.picocore import PicoCore


class BackButton(Button):

    def __init__(self, core, x, y):
        super().__init__(core, x, y, width=25, height=25)

    def on_click(self):
        PicoCore.get_scene_manager().set_current_scene("menu")

    def on_draw(self):
        Draw.change_color("#40e0d0")
        Draw.line(0, -12, 25, -12, width=2)
        Draw.line(0, -12, 12, 0, width=2)
        Draw.line(0, -12, 12, -25, width=2)
