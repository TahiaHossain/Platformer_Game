from __future__ import annotations

from abc import ABC, abstractmethod

from engine.component.component import Component
from engine.draw import Draw


class UiObject(ABC):
    def __init__(self, core, x, y, width=100, height=100, scale=1.0, rotation=0.0, debug=False):
        self.x = x
        self.y = y
        self.scale = scale
        self.rotation = rotation
        self.core = core
        self.started = False
        self.to_remove = False
        self.debug = debug

        self.width = width
        self.height = height
        self.top = self.y
        self.left = self.x
        self.right = self.x + self.width
        self.bottom = self.y - self.height

    @abstractmethod
    def on_start(self):
        pass

    @abstractmethod
    def on_update(self, delta_time):
        pass

    @abstractmethod
    def on_draw(self):
        pass

    def start(self):
        self.on_start()

    def update(self, delta_time):
        self.top = self.y
        self.left = self.x
        self.right = self.x + self.width
        self.bottom = self.y - self.height

        self.on_update(delta_time)

    def draw(self):
        self.on_draw()
        if self.debug:
            Draw.change_color("#FF0000")
            Draw.rect(0, 0, self.width, self.height)


class GameObject(ABC):
    def __init__(self, core, x, y, width, height, scale=1.0, rotation=0.0, debug=False):
        self.x = x
        self.y = y
        self.scale = scale
        self.rotation = rotation
        self.core = core
        self.parent = None
        self.children = []
        self.components = []
        self.started = False
        self.to_remove = False
        self.debug = debug

        self.width = width
        self.height = height
        self.top = self.y
        self.left = self.x
        self.right = self.x + self.width
        self.bottom = self.y - self.height

    @abstractmethod
    def on_start(self):
        pass

    @abstractmethod
    def on_update(self, delta_time):
        pass

    @abstractmethod
    def on_draw(self):
        pass

    def start(self):
        self.on_start()
        for component in self.components:
            component.start()

    def update(self, delta_time):
        self.top = self.y
        self.left = self.x
        self.right = self.x + self.width
        self.bottom = self.y - self.height

        for component in self.components:
            component.update(delta_time)
        self.on_update(delta_time)

    def draw(self):
        camera = self.core.get_scene_manager().get_current_scene().camera
        if self.right < camera.position[0] or \
                self.left > camera.position[0] + self.core.width or \
                self.top < camera.position[1] or \
                self.bottom > camera.position[1] + self.core.height:
            return
        self.on_draw()
        if self.debug:
            Draw.change_color("#FF0000")
            Draw.rect(0, 0, self.width, self.height)

    def add_child(self, child: GameObject):
        if child.parent is not None:
            child.parent.remove_child(child)
        child.parent = self
        self.children.append(child)

    def remove_child(self, child: GameObject):
        if child in self.children:
            self.children.remove(child)
            child.parent = None

    def add_component(self, component: Component):
        self.components.append(component)

    def remove_component(self, component: Component):
        if component in self.components:
            self.components.remove(component)

    def get_component(self, component_type):
        for component in self.components:
            if isinstance(component, component_type):
                return component
        return None
