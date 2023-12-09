from engine.camera import Camera
from engine.game_object import GameObject


class Scene:

    def __init__(self, engine):
        self.engine = engine
        self.game_objects: list[GameObject] = []
        self.ui_objects: list[GameObject] = []
        self.camera = Camera([0.0, 0.0], 1)
        self.paused = False

    def add_game_object(self, game_object: GameObject):
        self.game_objects.append(game_object)

    def remove_game_object(self, game_object: GameObject):
        if game_object in self.game_objects:
            self.game_objects.remove(game_object)

    def add_ui_object(self, game_object: GameObject):
        self.ui_objects.append(game_object)

    def remove_ui_object(self, ui_object: GameObject):
        if ui_object in self.ui_objects:
            self.ui_objects.remove(ui_object)
