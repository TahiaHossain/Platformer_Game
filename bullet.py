from engine.component.builtins import PhysicsComponent, ColliderComponent
from engine.draw import Draw
from engine.game_object import GameObject
from engine.picocore import PicoCore


class Bullet(GameObject):
    def __init__(self, core: PicoCore, x, y, width=10, height=10, debug=False):
        super().__init__(core, x, y, width, height, debug=debug)
        self.width = width
        self.height = height
        self.color = "#FFFFFF"
        self.top = y
        self.left = x
        self.right = x + width
        self.bottom = y - height

    def on_start(self):
        self.add_component(PhysicsComponent(self))
        self.add_component(ColliderComponent(self, self.width, self.height, static=True))

    def on_update(self, delta_time):
        physics_component: PhysicsComponent = self.get_component(PhysicsComponent)
        physics_component.velocity_x += 30 * delta_time

    def on_draw(self):
        Draw.change_color(self.color)
        Draw.rect(0, 0, self.width, self.height)
