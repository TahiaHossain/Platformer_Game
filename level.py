from back_button import BackButton
from block import Block
from fruit import Fruit
from enemy import EnemyOne, EnemyTwo, EnemyThree
from engine.button import Button
from engine.game_object import UiObject
from engine.draw import Draw
from engine.picocore import PicoCore
from engine.scene.scene import Scene
from player import Player
from random import randint, choice, getrandbits

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

class Ability(UiObject):
    def __init__(self, core, x, y, ability, player):
        super().__init__(core, x, y)
        self.ability = ability
        self.player = player
        self.status = player.abilities[ability]
        
    def on_start(self):
        pass

    def on_update(self, delta_time):
        self.status = self.player.abilities[self.ability]

    def on_draw(self):
        Draw.change_color("#FFFFFF")
        Draw.text(self.ability, self.x, self.y, size=20)
        if self.status:
            Draw.change_color("#00FF00")
        else:
            Draw.change_color("#FF0000")
        Draw.change_color("#FFFFFF")
        Draw.circle(self.x + 100, self.y - 10, 3, False)

def get_level_scene(engine: PicoCore) -> Scene:
    level = Scene(engine)

    player = Player(engine, 100, 500, debug=True)
    enemy = EnemyOne(engine, 200, 200, 100, 100)

    play_pause_button = PlayPauseButton(engine, engine.width / 2, engine.height - 50)
    double_jump_ability = Ability(engine, engine.width / 4, engine.height - 50, "double_jump", player)
    # dash_ability = Ability(engine, 50, engine.height - 100, "dash", player)
    
    level.add_game_object(player)
    for i in range(50):
        x_space = randint(100, 200)
        y_space = randint(100, 200)
        falling = bool(getrandbits(1))
        
        level.add_game_object(Block(engine, (i * 300) + x_space, y_space, width=200, height=50, falling=falling))
        if i % 4 == 0:
            enemy = choice((enemy_types))(engine, (i * 300) + x_space, y_space + 50, 100, 100, debug=True)
            level.add_game_object(enemy)

    level.add_game_object(Fruit(engine, 400, 300))

    level.add_ui_object(play_pause_button)
    level.add_ui_object(BackButton(engine, 40, engine.height - 50))
    # level.add_ui_object(dash_ability)
    
    level.camera.follow(player, 300, 300)
    return level
