from engine.component.builtins import ColliderComponent, PhysicsComponent, RigidBodyComponent
from engine.draw import Draw
from engine.game_object import GameObject


class Block(GameObject):
    def __init__(self, core, x, y, width=200, height=50, falling=False, debug=False):
        super().__init__(core, x, y, width, height, debug=debug)
        self.width = width
        self.height = height
        self.falling = falling

        self.top = y
        self.left = x
        self.right = x + width
        self.bottom = y - height

    def on_start(self):
        self.add_component(PhysicsComponent(self))
        self.add_component(ColliderComponent(self, self.width, self.height, static=True))
        rigidbody_component = RigidBodyComponent(self, gravity=1000)
        rigidbody_component.enabled = False
        self.add_component(rigidbody_component)

    def on_update(self, delta_time):
        rigidbody_component: RigidBodyComponent = self.get_component(RigidBodyComponent)
        collider_component: ColliderComponent = self.get_component(ColliderComponent)
        physics_component: PhysicsComponent = self.get_component(PhysicsComponent)

        if physics_component is not None:
            if len(physics_component.collisions) > 0 and collider_component is not None:
                if self.falling:
                    rigidbody_component.enabled = True

    def on_draw(self):
        Draw.change_color("#FFFFFF")
        Draw.rect(0, 0, self.width, self.height)
