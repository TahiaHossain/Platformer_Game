from abc import ABC, abstractmethod

from engine.game_object import GameObject, UiObject
from engine.input import Keys
from engine.picocore import PicoCore


class Button(UiObject, ABC):

    def __init__(self, core, x, y, width, height):
        super().__init__(core, x, y, width, height)
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
            print(position)

            if self.x < position[0] < self.x + self.width \
                    and self.y > position[1] > self.y - self.height:
                self.on_click()

        if self.processing_click:
            self.processing_clock += delta_time

        if self.processing_clock >= 500:
            self.processing_click = False
            self.processing_clock = 0

    @abstractmethod
    def on_click(self):
        pass

    @abstractmethod
    def on_draw(self):
        pass
