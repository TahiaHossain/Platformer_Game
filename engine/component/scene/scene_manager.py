from typing import Optional

from engine.component.scene.scene import Scene
from engine.utils import get_key_by_value


class SceneManager:

    def __init__(self, engine):
        self.engine = engine
        self.scenes = {}
        self.current_scene: Optional[Scene] = None

    def add_scene(self, tag: str, scene: Scene, set_current=False, pop=False):
        self.scenes[tag] = scene

        current_scene = self.current_scene

        if set_current or pop:
            self.current_scene = scene

        if pop:
            current_scene_key = get_key_by_value(self.scenes, current_scene)
            del self.scenes[current_scene_key]

    def remove_scene(self, tag: str):
        if tag in self.scenes:
            del self.scenes[tag]

    def get_current_scene(self) -> Scene:
        if self.current_scene is None:
            raise Exception("Cannot get current scene. No scene is set.")
        return self.current_scene

    def set_current_scene(self, tag: str):
        if tag in self.scenes:
            self.current_scene = self.scenes[tag]
        else:
            raise Exception("Invalid scene tag")
