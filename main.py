from engine.picocore import PicoCore

from level import get_level_scene
from main_menu import get_main_menu


PLATFORM_SIZE = 50
WIDTH = 700
HEIGHT = 500

engine = PicoCore("Platformer", WIDTH, HEIGHT)

level_one = get_level_scene(engine)
main_menu = get_main_menu(engine)

engine.get_scene_manager().add_scene("level_one", level_one)
engine.get_scene_manager().add_scene("menu", main_menu, set_current=True)

engine.run()
