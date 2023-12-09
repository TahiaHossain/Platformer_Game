from engine.component.builtins import ColliderComponent, PhysicsComponent
from engine.draw import Draw
from engine.game_object import GameObject
from engine.input import Keys
from engine.picocore import PicoCore

class Platform(GameObject):
    def __init__(self, core, x, y, width=50, height=50):
        super().__init__(core, x, y)
        self.width = width
        self.height = height
        
        self.top = y
        self.left = x
        self.right = x + width
        self.bottom = y - height
        
    def on_start(self):
        # self.add_component(PhysicsComponent(self))
        self.add_component(ColliderComponent(self, self.width, self.height))
        
    def on_update(self, delta_time):
        pass    

    def on_draw(self):
        Draw.change_color("#FFFFFF")
        Draw.rect(0, 0, self.width, self.height)
