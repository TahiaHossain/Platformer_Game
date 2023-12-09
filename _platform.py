from engine.component.builtins import ColliderComponent, PhysicsComponent
from engine.draw import Draw
from engine.game_object import GameObject


class Platform(GameObject):
    def __init__(self, core, x, y, width=200, height=50, debug=False):
        super().__init__(core, x, y, width, height, debug=debug)
        self.width = width
        self.height = height

        self.top = y
        self.left = x
        self.right = x + width
        self.bottom = y - height

    def on_start(self):
        self.add_component(ColliderComponent(self, self.width, self.height))
        
    def on_update(self, delta_time):
        pass

    def on_draw(self):
        Draw.change_color("#FFFFFF")
        Draw.rect(0, 0, self.width, self.height)
