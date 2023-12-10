from engine.component.builtins import RigidBodyComponent, PhysicsComponent, ColliderComponent
from engine.draw import Draw
from engine.game_object import GameObject
from engine.input import Keys
from engine.picocore import PicoCore
from bullet import Bullet
import time


class Player(GameObject):
    def __init__(self, core, x, y, width=30, height=80, debug=False):
        super().__init__(core, x, y, width, height, debug=debug)
        self.processing_click = False
        self.processing_clock = 0

        self.height = height
        self.width = width
        self.jump_counter = 0
        self.dead = False
        self.speed = 2

        self.abilities = {
            "double_jump": True,
            "dash": True,
        }
        self.health = 1
        self.score = 0
        self.last_dash = time.time()

    def jump(self, physics_component: PhysicsComponent, delta_time):
        self.jump_counter += 1
        if self.jump_counter > 1:
            self.abilities["double_jump"] = False

        if self.abilities["double_jump"]:
            physics_component.velocity_y += 50 * delta_time

    def dash(self, physics_component: PhysicsComponent, delta_time):
        if self.abilities["dash"]:
            self.last_dash = time.time()
            physics_component.velocity_x += 100 * delta_time
            self.abilities["dash"] = False

    def on_start(self):
        self.add_component(PhysicsComponent(self))
        self.add_component(RigidBodyComponent(self, gravity=2000))
        self.add_component(ColliderComponent(self, self.width, self.height))
        self.scene = self.core.get_scene_manager().get_current_scene()

    def handle_shooting(self, delta_time):
        if PicoCore.is_pressed(Keys.LMB) and not self.processing_click:
            self.processing_click = True
            self.scene.add_game_object(Bullet(self.core, self.x + 30, self.y))

        if self.processing_click:
            self.processing_clock += delta_time

        if self.processing_clock >= 500:
            self.processing_click = False
            self.processing_clock = 0

    def handle_controls(self, physics_component: PhysicsComponent, delta_time):
        # Vertical Movement
        if PicoCore.is_pressed(Keys.d):
            physics_component.velocity_x += self.speed * delta_time
        elif PicoCore.is_pressed(Keys.a):
            physics_component.velocity_x -= self.speed * delta_time

        # Jump
        if PicoCore.is_pressed(Keys.SPACE, hold=False):
            self.jump(physics_component, delta_time)

        # Dash
        if PicoCore.is_pressed(Keys.e, hold=False):
            self.dash(physics_component, delta_time)

    def on_update(self, delta_time):
        physics_component: PhysicsComponent = self.get_component(PhysicsComponent)
        collider_component: ColliderComponent = self.get_component(ColliderComponent)

        if self.y < -50:
            self.health = 0

        if self.health <= 0:
            self.dead = True
            self.scene.paused = True

        if physics_component is not None:

            if time.time() - self.last_dash > 1:
                self.abilities["dash"] = True

            self.handle_controls(physics_component, delta_time)
            self.handle_shooting(delta_time)

    def on_draw(self):
        Draw.change_color("#ffc0cb")
        if self.dead:
            Draw.change_color("#FF0000")
        Draw.circle(25, -12, -20, False, 3)
        Draw.circle(25, -12, -20, False, 3)
        Draw.circle(25, -12, -20, False, 3)

        Draw.line(8, -20, -22, -60)
        Draw.line(18, -20, 48, -60)
        Draw.line(-22, -60, 48, -60)
        if self.dead:
            Draw.text("X", 0, 15)
            Draw.text("X", 15, 15)
        else:
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
        Draw.circle(5, 8, -10, 3)
        # legs
        Draw.circle(10, -12, -77, False, 3)
        Draw.circle(10, 17, -77, False, 3)
