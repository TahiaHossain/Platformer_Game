from engine.button import Button
from engine.draw import Draw
from engine.label import Label
from engine.picocore import PicoCore
from engine.scene.scene import Scene


class PlayOption(Button):

    def __init__(self, core, x, y):
        super().__init__(core, x, y, width=100, height=40)

    def on_click(self):
        self.core.get_scene_manager().set_current_scene("level_one")

    def on_draw(self):
        Draw.change_color("#2FF518")
        Draw.rect(0, 0, self.width, self.height)

        Draw.line(10, -7, 10, -32, width=2)
        Draw.line(10, -7, 35, -19, width=2)
        Draw.line(10, -32, 35, -19, width=2)

        Draw.text("PLAY", 45, -16, size=8)


def get_main_menu(engine: PicoCore) -> Scene:
    main_menu = Scene(engine)

    main_menu.add_game_object(
        Label(engine, "PLATFORMER", (engine.width / 2), (engine.height / 2) + 100, alignment="center"))
    main_menu.add_game_object(PlayOption(engine, (engine.width / 2) - 50, engine.height / 2))

    return main_menu
