from __future__ import annotations

from abc import ABC, abstractmethod
from engine.component.component import Component


class GameObject(ABC):
    def __init__(self, core, x=0, y=0, scale=1.0, rotation=0.0):
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
        self.on_update(delta_time)
        for component in self.components:
            component.update(delta_time)

    def draw(self):
        self.on_draw()

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
