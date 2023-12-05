from engine.component.builtins import RigidBodyComponent, PhysicsComponent, ColliderComponent
from engine.draw import Draw
from engine.game_object import GameObject
from engine.input import Keys
from engine.picocore import PicoCore
from _platform import Platform
from floor import Floor
class Player(GameObject):

    def __init__(self, core, x, y, height=80, width=20):
        super().__init__(core, x, y)
        self.height = height
        self.width = width
        self.jump_counter = 0
        
        self.abilities = {
            "double_jump": True,
        }

    def jump(self, physics_component: PhysicsComponent, delta_time):
        self.jump_counter += 1
        if self.abilities["double_jump"] and self.jump_counter < 1000:
            physics_component.velocity_y += 70 * delta_time
            
    def on_start(self):
        self.add_component(PhysicsComponent(self))
        self.add_component(RigidBodyComponent(self, gravity=2000))
        self.add_component(ColliderComponent(self, 20, 80))
    
    def on_update(self, delta_time):
        self.top = self.y
        self.left = self.x
        self.right = self.x + self.width
        self.bottom = self.y - self.height
        
        physics_component: PhysicsComponent = self.get_component(PhysicsComponent)
        collider_component: ColliderComponent = self.get_component(ColliderComponent)

        if physics_component is not None:
            if PicoCore.is_pressed(Keys.d):
                physics_component.velocity_x += 1 * delta_time
            elif PicoCore.is_pressed(Keys.a):
                physics_component.velocity_x -= 1 * delta_time
            if PicoCore.is_pressed(Keys.SPACE, hold=False):
                self.jump(physics_component, delta_time)

            if len(physics_component.collisions) > 0 and collider_component is not None:
                collided_with = physics_component.collisions[0]
                other_collider = collided_with.get_component(ColliderComponent)
                
                if isinstance(collided_with, Platform):
                    self.jump_counter = 0
                    self.y = collided_with.top + self.height

    def on_draw(self):
        Draw.change_color("#FFFFFF")
        Draw.rect(0, 0, self.width, self.height)
