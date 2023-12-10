from block import Block
from engine.component.builtins import RigidBodyComponent, PhysicsComponent, ColliderComponent
from engine.draw import Draw
from engine.game_object import GameObject


class Enemy(GameObject):
    def __init__(self, core, x, y, height=80, width=20, debug=False):
        super().__init__(core, x, y, width, height, debug=debug)
        self.height = height
        self.width = width

    def on_start(self):
        self.add_component(PhysicsComponent(self))
        # self.add_component(RigidBodyComponent(self, gravity=2000))
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


class EnemyOne(Enemy):
    def __init__(self, core, x, y, height=80, width=20, debug=False):
        super().__init__(core, x, y, width, height, debug=debug)

    def on_draw(self):
        Draw.change_color("#FF0000")
        Draw.rect(0, 0, 45, 45)
        Draw.rect(25, -45, 80, 40)
        # legs
        Draw.rect(40, -85, 15, 15, False)
        Draw.rect(75, -85, 15, 15, False)
        # tail
        Draw.circle(7, 100, -50, False, thickness=3)
        # eyes
        Draw.rect(7, -10, 10, 10, False)
        Draw.rect(25, -10, 10, 10, False)
        # mouth
        Draw.rect(12, -30, 20, 5, False)
        # hair
        Draw.line(0, 0, 15, 10)
        Draw.line(10, 0, 25, 10)
        Draw.line(20, 0, 35, 10)
        Draw.line(30, 0, 45, 10)
        Draw.line(40, 0, 55, 10)


class EnemyTwo(Enemy):
    def __init__(self, core, x, y, height=80, width=20, debug=False):
        super().__init__(core, x, y, width, height, debug=debug)

    def on_draw(self):
        # enemy 2
        Draw.change_color("#FF00FF")
        Draw.rect(12, 0, 45, 45)
        Draw.rect(20, -45, 30, 40)
        # leg
        Draw.rect(10, -85, 50, 15, False)
        # eyes
        Draw.rect(20, -10, 10, 10, False)
        Draw.rect(38, -10, 10, 10, False)
        # mouth
        Draw.rect(25, -30, 20, 5, False)
        # hair
        Draw.line(12, 0, 20, 30)
        Draw.line(57, 0, 50, 30)
        Draw.circle(5, 15, 30, False, 3)
        Draw.circle(5, 45, 30, False, 3)
        Draw.line(25, 0, 30, 20)
        Draw.line(45, 0, 40, 20)
        Draw.circle(3, 27, 20, False, 3)
        Draw.circle(3, 37, 20, False, 3)


class EnemyThree(Enemy):
    def __init__(self, core, x, y, height=80, width=20, debug=False):
        super().__init__(core, x, y, width, height, debug=debug)

    def on_draw(self):
        # enemy 3
        Draw.change_color("#00FFFF")
        Draw.rect(12, 0, 45, 45)
        Draw.rect(20, -45, 30, 40)
        # leg
        Draw.rect(10, -85, 50, 15, False)
        # eyes
        Draw.rect(20, -10, 10, 10, False)
        Draw.rect(38, -10, 10, 10, False)
        # mouth
        Draw.rect(25, -30, 20, 5, False)
        # hair
        Draw.line(12, 0, 18, 30)
        Draw.line(23, 0, 18, 30)
        Draw.line(23, 0, 30, 30)
        Draw.line(35, 0, 30, 30)
        Draw.line(35, 0, 42, 30)
        Draw.line(47, 0, 42, 30)
        Draw.line(47, 0, 53, 30)
        Draw.line(57, 0, 53, 30)
