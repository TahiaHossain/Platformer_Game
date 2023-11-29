from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, game_object):
        self.game_object = game_object
        self.enabled = True

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self, delta_time):
        pass
