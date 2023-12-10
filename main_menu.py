from engine.button import Button
from engine.draw import Draw
from engine.label import Label
from engine.picocore import PicoCore
from engine.scene.scene import Scene
from level import get_level_scene
from scores import get_scores_scene


class PlayOption(Button):

    def __init__(self, core, x, y):
        super().__init__(core, x, y, width=140, height=40)

    def on_click(self):
        self.core.get_scene_manager().add_scene("level_one", get_level_scene(self.core), set_current=True)

    def on_draw(self):
        Draw.change_color("#2FF518")
        Draw.rect(0, 0, self.width, self.height)

        Draw.line(10, -7, 10, -32, width=2)
        Draw.line(10, -7, 35, -19, width=2)
        Draw.line(10, -32, 35, -19, width=2)

        Draw.text("PLAY", 55, -16, size=8)


class ScoreOption(Button):

    def __init__(self, core, x, y):
        super().__init__(core, x, y, width=140, height=40)

    def on_click(self):
        self.core.get_scene_manager().add_scene("scores", get_scores_scene(self.core), set_current=True)

    def on_draw(self):
        Draw.change_color("#33E6FF")
        Draw.rect(0, 0, self.width, self.height)

        Draw.line(10, -7, 10, -32, width=4)
        Draw.line(18, -11, 18, -32, width=4)
        Draw.line(26, -15, 26, -32, width=4)

        Draw.text("SCORES", 55, -16, size=8)


class ExitOption(Button):

    def __init__(self, core, x, y):
        super().__init__(core, x, y, width=140, height=40)

    def on_click(self):
        self.core.exit()

    def on_draw(self):
        Draw.change_color("#FF0000")
        Draw.rect(0, 0, self.width, self.height)
        Draw.line(10, -7, 35, -32, width=2)
        Draw.line(35, -7, 10, -32, width=2)
        Draw.text("CLOSE", 55, -16, size=8)


def get_main_menu(engine: PicoCore) -> Scene:
    main_menu = Scene(engine)

    main_menu.add_ui_object(Label(
        engine,
        "PLATFORMER",
        (engine.width / 2),
        (engine.height / 2) + 100,
        alignment="center")
    )
    main_menu.add_ui_object(PlayOption(engine, (engine.width / 2) - 70, engine.height / 2))
    main_menu.add_ui_object(ScoreOption(engine, (engine.width / 2) - 70, (engine.height / 2) - 50))
    main_menu.add_ui_object(ExitOption(engine, (engine.width / 2) - 70, (engine.height / 2) - 100))

    return main_menu
