from engine.component.builtins import RigidBodyComponent, PhysicsComponent, ColliderComponent
from engine.draw import Draw
from engine.game_object import GameObject
from engine.input import Keys
from engine.picocore import PicoCore
from platform import Platform
from floor import Floor


class Player(GameObject):

    def __init__(self, core, x, y, width=30, height=80, debug=False):
        super().__init__(core, x, y, width, height, debug=debug)

        self.height = height
        self.width = width
        self.jump_counter = 0

        self.abilities = {
            "double_jump": True,
        }

    def jump(self, physics_component: PhysicsComponent, delta_time):
        self.jump_counter += 1
        if self.abilities["double_jump"] and self.jump_counter < 3:
            physics_component.velocity_y += 50 * delta_time

    def on_start(self):
        self.add_component(PhysicsComponent(self))
        self.add_component(RigidBodyComponent(self, gravity=2000))
        self.add_component(ColliderComponent(self, self.width, self.height))


    def on_update(self, delta_time):
        physics_component: PhysicsComponent = self.get_component(PhysicsComponent)
        collider_component: ColliderComponent = self.get_component(ColliderComponent)

        if physics_component is not None:

            if len(physics_component.collisions) > 0 and collider_component is not None:
                collided_with = physics_component.collisions[0]

                if isinstance(collided_with, Platform):
                    self.jump_counter = 0

            if PicoCore.is_pressed(Keys.d):
                physics_component.velocity_x += 1 * delta_time
            elif PicoCore.is_pressed(Keys.a):
                physics_component.velocity_x -= 1 * delta_time
            if PicoCore.is_pressed(Keys.SPACE, hold=False):
                self.jump(physics_component, delta_time)

    def on_draw(self):
        Draw.change_color("#ffc0cb")

        Draw.circle(25, -12, -20)
        Draw.circle(25, -12, -20)
        Draw.circle(25, -12, -20)

        Draw.line(8, -20, -22, -60)
        Draw.line(18, -20, 48, -60)
        Draw.line(-22, -60, 48, -60)
        # left eye
        Draw.line(7, 16, 0, 8)
        Draw.line(7, 16, 10, 8)
        # right eye
        Draw.line(23, 16, 17, 8)
        Draw.line(23, 16, 27, 8)
        # left beard
        Draw.line(8, -2, -24, 10)
        Draw.line(8, -4, -24, 0)
        Draw.line(8, -6, -24, -10)
        # right beard
        Draw.line(17, -2, 49, 10)
        Draw.line(17, -4, 49, 0)
        Draw.line(17, -6, 49, -10)
        # tail
        Draw.line(-12, -45, -30, -40)
        # nose
        Draw.circle(5, 8, -10, fill=False)
        # legs
        Draw.circle(10, -12, -77, fill=False)
        Draw.circle(10, 17, -77, fill=False)

