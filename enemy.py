from engine.component.builtins import RigidBodyComponent, PhysicsComponent, ColliderComponent
from engine.draw import Draw
from engine.game_object import GameObject
from engine.picocore import PicoCore
from _platform import Platform

class Enemy(GameObject):
    def __init__(self, core, x, y, height=80, width=20):
        super().__init__(core, x, y)
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

                if isinstance(collided_with, Platform):
                    self.y = collided_with.top + self.height

    def on_draw(self):
        pass

class EnemyOne(Enemy):
    def __init__(self, core, x, y, height=80, width=20):
        super().__init__(core, x, y)
        
    def on_draw(self):
        Draw.change_color("#FF0000")
        Draw.rect(50, 20, 45, 45)
        Draw.rect(75, -25, 80, 40)
        # legs
        Draw.rect(90, -65, 15, 15)
        Draw.rect(125, -65, 15, 15)
        # tail
        Draw.circle(7, 150, -30, thickness=3)
        # eyes
        Draw.rect(57, 10, 10, 10)
        Draw.rect(75, 10, 10, 10)
        # mouth
        Draw.rect(62, -10, 20, 5)
        # hair
        Draw.line(50, 20, 65, 30)
        Draw.line(60, 20, 75, 30)
        Draw.line(70, 20, 85, 30)
        Draw.line(80, 20, 95, 30)
        Draw.line(90, 20, 105, 30)


class EnemyTwo(Enemy):
    def __init__(self, core, x, y, height=80, width=20):
        super().__init__(core, x, y)
        
    def on_draw(self):
        # enemy 2
        Draw.change_color("#FF00FF")
        Draw.rect(212, 20, 45, 45)
        Draw.rect(220, -25, 30, 40)
        # leg
        Draw.rect(210, -65, 50, 15)
        # eyes
        Draw.rect(220, 10, 10, 10)
        Draw.rect(238, 10, 10, 10)
        # mouth
        Draw.rect(225, -10, 20, 5)
        # hair
        Draw.line(212, 20, 220, 50)
        Draw.line(257, 20, 250, 50)
        Draw.circle(5, 215, 50, False, 3)
        Draw.circle(5, 245, 50, False, 3)
        Draw.line(225, 20, 230, 40)
        Draw.line(245, 20, 240, 40)
        Draw.circle(3, 227, 40, False, 3)
        Draw.circle(3, 237, 40, False, 3)


class EnemyThree(Enemy):
    def __init__(self, core, x, y, height=80, width=20):
        super().__init__(core, x, y)
            
    def on_draw(self):
        # enemy 3
        Draw.change_color("#00FFFF")
        Draw.rect(312, 20, 45, 45)
        Draw.rect(320, -25, 30, 40)
        # leg
        Draw.rect(310, -65, 50, 15)
        # eyes
        Draw.rect(320, 10, 10, 10)
        Draw.rect(338, 10, 10, 10)
        # mouth
        Draw.rect(325, -10, 20, 5)
        # hair
        Draw.line(312, 20, 318, 50)
        Draw.line(323, 20, 318, 50)
        Draw.line(323, 20, 330, 50)
        Draw.line(335, 20, 330, 50)
        Draw.line(335, 20, 342, 50)
        Draw.line(347, 20, 342, 50)
        Draw.line(347, 20, 353, 50)
        Draw.line(357, 20, 353, 50)
