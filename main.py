from engine.draw import Draw
from engine.game_object import GameObject
from engine.picocore import PicoCore

engine = PicoCore("Platformer", 700, 500)


class Test(GameObject):

    def on_start(self):
        pass

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        Draw.text("HELLO WORLD", 0, 0)


test = Test(engine, (engine.width / 2) - 100, engine.height / 2)
engine.add_game_object(test)
engine.run()
