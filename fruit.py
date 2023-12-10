from engine.component.builtins import RigidBodyComponent, PhysicsComponent, ColliderComponent
from engine.draw import Draw
from engine.game_object import GameObject
from engine.picocore import PicoCore
from block import Block

class Fruit(GameObject):
    def __init__(self, core, x, y, height=80, width=20, debug=False):
        super().__init__(core, x, y, width, height, debug=debug)
        self.height = height
        self.width = width

    def on_start(self):
        self.add_component(PhysicsComponent(self))
        self.add_component(RigidBodyComponent(self, gravity=2000))
        self.add_component(ColliderComponent(self, self.width, self.height))

    def on_update(self, delta_time):
        self.top = self.y
        self.left = self.x
        self.right = self.x + self.width
        self.bottom = self.y - self.height

        physics_component: PhysicsComponent = self.get_component(PhysicsComponent)
        collider_component: ColliderComponent = self.get_component(ColliderComponent)

        if physics_component is not None:
            if len(physics_component.collisions) > 0 and collider_component is not None:
                collided_with = physics_component.collisions[0]
                other_collider = collided_with.get_component(ColliderComponent)

                if isinstance(collided_with, Block):
                    self.y = collided_with.top + self.height

    def on_draw(self):
        pass

class Fruit(Fruit):
    def __init__(self, core, x, y, height=80, width=20, debug=False):
        super().__init__(core, x, y, width, height, debug=debug)
        
    def on_draw(self):
        Draw.change_color("#FFFF00")
        Draw.rect(20, -10, 30, 30)
        Draw.rect(12, 10, 5, 5, True)
        