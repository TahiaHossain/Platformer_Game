from engine.component.builtins import RigidBodyComponent, PhysicsComponent
from engine.draw import Draw
from engine.game_object import GameObject
from engine.input import Keys
from engine.picocore import PicoCore


class Player(GameObject):

    def __init__(self, core, x, y):
        super().__init__(core, x, y)

    def on_start(self):
        self.add_component(PhysicsComponent(self))
        self.add_component(RigidBodyComponent(self))

    def on_update(self, delta_time):
        physics_component: PhysicsComponent = self.get_component(PhysicsComponent)

        if physics_component is not None:
            if PicoCore.is_pressed(Keys.d):
                physics_component.velocity_x += 1 * delta_time
            elif PicoCore.is_pressed(Keys.a):
                physics_component.velocity_x -= 1 * delta_time
            if PicoCore.is_pressed(Keys.SPACE):
                physics_component.velocity_y += 10 * delta_time

    def on_draw(self):
        Draw.change_color("#FFFFFF")
        Draw.rect(0, 0, 20, 80)
