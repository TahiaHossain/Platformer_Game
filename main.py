from engine.draw import Draw
from engine.game_object import GameObject
from engine.picocore import PicoCore
from player import Player
from enemy import Enemy

engine = PicoCore("Platformer", 700, 500)


class Test(GameObject):

    def on_start(self):
        pass

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        Draw.change_color("#FFFFFF")
        Draw.text("HELLO WORLD", 0, 0, size=20)


test = Test(engine, (engine.width / 2) - 100, engine.height / 2)

player = Player(engine, 100, 400)
enemy = Enemy(engine, 200, 200)

engine.add_game_object(test)
engine.add_game_object(player)
engine.add_game_object(enemy)
engine.run()
