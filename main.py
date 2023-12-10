from engine.picocore import PicoCore

from level import get_level_scene
from main_menu import get_main_menu
from scores import get_scores_scene

PLATFORM_SIZE = 50
WIDTH = 900
HEIGHT = 700

engine = PicoCore("Platformer", WIDTH, HEIGHT)

level_one = get_level_scene(engine)
main_menu = get_main_menu(engine)
scores = get_scores_scene(engine)

engine.get_scene_manager().add_scene("level_one", level_one)
engine.get_scene_manager().add_scene("scores", scores)
engine.get_scene_manager().add_scene("menu", main_menu, set_current=True)

engine.run()
