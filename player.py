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
        Draw.change_color("#ffc0cb")
        Draw.circle(25,-20,-20)
        Draw.circle(25,-20,-20)
        Draw.circle(25,-20,-20)
        
        Draw.line(0,-20,-30,-60)
        Draw.line(10,-20,40,-60)
        Draw.line(-30,-60,40,-60)
        # left eye
        Draw.line(-2,16,-8,8)
        Draw.line(-2,16,2,8)
        # right eye
        Draw.line(14,16,8,8)
        Draw.line(14,16,18,8)
        # left beard
        Draw.line(2,-2,-30,10)
        Draw.line(2,-4,-30,0)
        Draw.line(2,-6,-30,-10)
        # right beard
        Draw.line(8,-2,40,10)
        Draw.line(8,-4,40,0)
        Draw.line(8,-6,40,-10)
        # tail
        Draw.line(-22,-45,-40,-40)
        # nose
        Draw.circle(5, 0, -10, fill=True)
        # legs
        Draw.circle(10, -20, -77, fill=True)
        Draw.circle(10, 10, -77, fill=True)


        # enemy 1   
        Draw.change_color("#FF0000")
        Draw.rect(75, 20, 45, 45)
        Draw.rect(100, -25, 80, 40)
        # legs
        Draw.rect(115, -65, 15, 15, fill=True)
        Draw.rect(150, -65, 15, 15, fill=True)
        # tail
        Draw.circle(7, 175, -30, fill=True)
        # eyes
        Draw.rect(82, 10, 10, 10, fill=True)
        Draw.rect(100, 10, 10, 10, fill=True)
        # mouth
        Draw.rect(87, -10, 20, 5, fill=True)
        # hair
        Draw.line(75, 20, 90, 30)
        Draw.line(85, 20, 100, 30)
        Draw.line(95, 20, 110, 30)
        Draw.line(105, 20, 120, 30)
        Draw.line(115, 20, 130, 30)


        # enemy 2
        Draw.change_color("#FF00FF")
        Draw.rect(212, 20, 45, 45)
        Draw.rect(220, -25, 30, 40)
        # leg
        Draw.rect(210, -65, 50, 15, fill=True)
        # eyes
        Draw.rect(220, 10, 10, 10, fill=True)
        Draw.rect(238, 10, 10, 10, fill=True)
        # mouth
        Draw.rect(225, -10, 20, 5, fill=True)
        # hair
        Draw.line(212, 20, 220, 50)
        Draw.line(257, 20, 250, 50)
        Draw.circle(5, 215, 50)
        Draw.circle(5, 245, 50)
        Draw.line(225, 20, 230, 40)
        Draw.line(245, 20, 240, 40)
        Draw.circle(3, 227, 40)
        Draw.circle(3, 237, 40)


        # enemy 3
        Draw.change_color("#00FFFF")
        Draw.rect(312, 20, 45, 45)
        Draw.rect(320, -25, 30, 40)
        # leg
        Draw.rect(310, -65, 50, 15, fill=True)
        # eyes
        Draw.rect(320, 10, 10, 10, fill=True)
        Draw.rect(338, 10, 10, 10, fill=True)
        # mouth
        Draw.rect(325, -10, 20, 5, fill=True)
        # hair
        Draw.line(312, 20, 318, 50)
        Draw.line(323, 20, 318, 50)
        Draw.line(323, 20, 330, 50)
        Draw.line(335, 20, 330, 50)
        Draw.line(335, 20, 342, 50)
        Draw.line(347, 20, 342, 50)
        Draw.line(347, 20, 353, 50)
        Draw.line(357, 20, 353, 50)