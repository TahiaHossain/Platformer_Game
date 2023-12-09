from _platform import Platform
from enemy import EnemyOne, EnemyTwo, EnemyThree
from engine.button import Button
from engine.draw import Draw
from engine.picocore import PicoCore
from engine.scene.scene import Scene
from player import Player
from random import randint, choice

enemy_types = [EnemyOne, EnemyTwo, EnemyThree]
class PlayPauseButton(Button):

    def __init__(self, core, x, y):
        super().__init__(core, x, y, width=25, height=25)
        self.paused = False

    def on_click(self):
        PicoCore.get_scene_manager().current_scene.paused = not PicoCore.get_scene_manager().current_scene.paused
        self.paused = PicoCore.get_scene_manager().current_scene.paused

    def on_draw(self):
        Draw.change_color("#2FF518")

        if self.paused:
            Draw.line(0, 0, 0, -25, width=2)
            Draw.line(0, 0, 20, -12, width=2)
            Draw.line(0, -25, 20, -12, width=2)
        else:
            Draw.line(0, 0, 0, -25, width=2)
            Draw.line(20, 0, 20, -25, width=2)


def get_level_scene(engine: PicoCore) -> Scene:
    level = Scene(engine)

    player = Player(engine, 100, 500, debug=False)
    enemy = EnemyOne(engine, 200, 200, 100, 100)

    play_pause_button = PlayPauseButton(engine, engine.width / 2, engine.height - 50)

    level.add_game_object(player)
    # level.add_game_object(enemy)
    for i in range(50):
        x_space = randint(100, 250)
        y_space = randint(100, 250)
        level.add_game_object(Platform(engine, (i * 200) + x_space, y_space, width=200, height=50))
        if i % 4 == 0:
            enemy = choice((enemy_types))(engine, (i * 200) + x_space, y_space + 50, 100, 100)
            level.add_game_object(enemy)
    level.add_ui_object(play_pause_button)
    level.camera.follow(player, 300, 300)

    return level
