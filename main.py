from abc import ABC, abstractmethod
from enemy import EnemyOne
from engine.component.scene.scene import Scene
from engine.draw import Draw
from engine.game_object import GameObject
from engine.input import Keys
from engine.picocore import PicoCore
from player import Player

PLATFORM_SIZE = 50
WIDTH = 700
HEIGHT = 500

engine = PicoCore("Platformer", WIDTH, HEIGHT)

player = Player(engine, 100, 500)
enemy = EnemyOne(engine, 200, 200)

level_one = Scene(engine)

level_one.add_game_object(player)
level_one.add_game_object(enemy)
level_one.camera.follow(player, 100, 100)

engine.get_scene_manager().add_scene("level_one", level_one)

main_menu = Scene(engine)


class PlayButton(GameObject):

    def __init__(self, core, x, y):
        super().__init__(core, x, y)
        self.processing_click = False
        self.processing_clock = 0

    def on_start(self):
        pass

    def on_update(self, delta_time):

        if PicoCore.is_pressed(Keys.LMB) and not self.processing_click:
            self.processing_click = True
            position = PicoCore.get_click_position()

            if self.x < position[0] < self.x + 25 \
                    and self.y > position[1] > self.y - 25:
                self.core.get_scene_manager().set_current_scene("level_one")

        if self.processing_click:
            self.processing_clock += delta_time

        if self.processing_clock >= 500:
            self.processing_click = False
            self.processing_clock = 0

    def on_draw(self):
        Draw.change_color("#F0DA20")
        Draw.line(0, 0, 0, -25, width=2)
        Draw.line(0, 0, 20, -12, width=2)
        Draw.line(0, -25, 20, -12, width=2)


class Button(GameObject, ABC):

    def __init__(self, core, x, y, width, height):
        super().__init__(core, x, y)
        self.width = width
        self.height = height
        self.processing_click = False
        self.processing_clock = 0

    def on_start(self):
        pass

    def on_update(self, delta_time):

        if PicoCore.is_pressed(Keys.LMB) and not self.processing_click:
            self.processing_click = True
            position = PicoCore.get_click_position()

            if self.x < position[0] < self.x + 25 \
                    and self.y > position[1] > self.y - 25:
                self.core.get_scene_manager().set_current_scene("level_one")

        if self.processing_click:
            self.processing_clock += delta_time

        if self.processing_clock >= 500:
            self.processing_click = False
            self.processing_clock = 0

    @abstractmethod
    def on_draw(self):
        pass







main_menu.add_game_object(PlayButton(engine, WIDTH / 2, HEIGHT / 2))

engine.get_scene_manager().add_scene("menu", main_menu, set_current=True)

engine.run()
