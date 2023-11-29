from __future__ import annotations
import math

from engine.component.component import Component
from engine.game_object import GameObject


class CircularMotionComponent(Component):
    def __init__(self, game_object, center_x, center_y, radius, angular_velocity):
        super().__init__(game_object)
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.angular_velocity = angular_velocity
        self.angle = 0

    def start(self):
        pass

    def update(self, delta_time):
        delta_time_seconds = delta_time / 1000.0
        self.angle += self.angular_velocity * delta_time_seconds

        self.game_object.x = self.center_x + self.radius * math.cos(self.angle)
        self.game_object.y = self.center_y + self.radius * math.sin(self.angle)


class ColliderComponent(Component):
    def start(self):
        pass

    def update(self, delta_time):
        pass

    def __init__(self, game_object, width: float, height: float):
        super().__init__(game_object)
        self.width = width
        self.height = height

    def collides_with(self, collider: ColliderComponent):

        if self.game_object.x + self.width < collider.game_object.x \
                or self.game_object.x > collider.game_object.x + collider.width \
                or self.game_object.y - self.height < collider.game_object.y \
                or self.game_object.y > collider.game_object.y + collider.height:
            return False
        else:
            return True


class CircularColliderComponent(ColliderComponent):
    def __init__(self, game_object, radius: float):
        super().__init__(game_object, radius * 2, radius * 2)
        self.radius = radius

    def collides_with(self, collider: ColliderComponent):
        if isinstance(collider, CircularColliderComponent):
            # Circle-circle collision detection
            dx = self.game_object.x - collider.game_object.x
            dy = self.game_object.y - collider.game_object.y
            distance = (dx ** 2 + dy ** 2) ** 0.5
            return distance < (self.radius + collider.radius)
        else:
            # Circle-AABB collision detection
            half_width = collider.width / 2
            half_height = collider.height / 2
            center_x = collider.game_object.x + half_width
            center_y = collider.game_object.y - half_height

            delta_x = self.game_object.x - center_x
            delta_y = self.game_object.y + self.radius - center_y

            test_x = abs(delta_x) - half_width - self.radius
            test_y = abs(delta_y) - half_height - self.radius

            if test_x > 0 or test_y > 0:
                return False

            if test_x <= -self.radius or test_y <= -self.radius:
                return True

            corner_distance_sq = test_x ** 2 + test_y ** 2

            return corner_distance_sq <= self.radius ** 2


class PhysicsComponent(Component):
    def __init__(self, game_object, velocity_x=0, velocity_y=0, friction=0.1):
        super().__init__(game_object)
        self.collider = None
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.friction = friction
        self.collisions = []

        if friction > 1.0 or friction < 0.0:
            raise Exception("Invalid friction value. Must be in a range of 0 to 1")

    def start(self):
        self.collider = self.game_object.get_component(ColliderComponent)

    def update(self, delta_time):
        if self.enabled:
            self.velocity_x *= (1 - self.friction)
            self.velocity_y *= (1 - self.friction)

            delta_time_seconds = delta_time / 1000

            self.game_object.x += self.velocity_x * delta_time_seconds
            self.game_object.y += self.velocity_y * delta_time_seconds

            self.handle_collisions()

    def handle_collisions(self):
        # Here you can check for collisions with other game objects, e.g., floors or walls
        for other_object in self.game_object.core.game_objects:
            if other_object == self.game_object:
                continue

            other_collider = other_object.get_component(ColliderComponent)

            if self.collider is not None and other_collider is not None and self.collider.collides_with(other_collider):
                # self.resolve_collision(other_object)
                if other_object not in self.collisions:
                    self.collisions.append(other_object)
            else:
                if other_object in self.collisions:
                    self.collisions.remove(other_object)

    def resolve_collision(self, other_object):
        # Prevent the game object from falling through the floor
        other_collider = other_object.get_component(ColliderComponent)

        if isinstance(self.collider, CircularColliderComponent) and isinstance(other_collider,
                                                                               CircularColliderComponent):
            # Circle-circle collision resolution
            # (not handling this case for now)
            pass
        elif isinstance(self.collider, CircularColliderComponent):
            # Circle-rectangle collision resolution
            dx = self.game_object.x - (other_object.x + other_collider.width / 2)
            dy = self.game_object.y - (other_object.y + other_collider.height / 2)
            half_width_sum = (self.collider.width + other_collider.width) / 2
            half_height_sum = (self.collider.height + other_collider.height) / 2

            if abs(dx) <= half_width_sum and abs(dy) <= half_height_sum:
                width_overlap = half_width_sum - abs(dx)
                height_overlap = half_height_sum - abs(dy)

                if width_overlap < height_overlap:
                    if dx > 0:
                        self.game_object.x += width_overlap
                    else:
                        self.game_object.x -= width_overlap
                    self.velocity_x *= -1
                else:
                    if dy > 0:
                        self.game_object.y += height_overlap
                    else:
                        self.game_object.y -= height_overlap
                    self.velocity_y = 0
        else:
            # Calculate the overlap in x and y
            dx = (self.game_object.x + self.collider.width / 2) - (other_object.x + other_collider.width / 2)
            dy = (self.game_object.y + self.collider.height / 2) - (other_object.y + other_collider.height / 2)

            width_overlap = (self.collider.width + other_collider.width) / 2 - abs(dx)
            height_overlap = (self.collider.height + other_collider.height) / 2 - abs(dy)

            # Determine the side of the collision and resolve it
            if width_overlap < height_overlap:
                if dx > 0:
                    self.game_object.x += width_overlap
                else:
                    self.game_object.x -= width_overlap
            else:
                if dy > 0:
                    self.game_object.y += height_overlap
                    self.velocity_y = 0
                else:
                    self.game_object.y -= height_overlap
                    self.velocity_y = 0


class RigidBodyComponent(Component):

    def __init__(self, game_object: GameObject, gravity=500, mass: float = 1.0):
        super().__init__(game_object)
        self.mass = mass
        self.gravity = gravity
        self.physics_component = self.game_object.get_component(PhysicsComponent)
        if self.physics_component is None:
            raise Exception("RigidBodyComponent requires a PhysicsComponent.")

    def start(self):
        pass

    def update(self, delta_time):
        # Apply gravity to the object
        delta_time_seconds = delta_time / 1000
        self.physics_component.velocity_y -= self.gravity * delta_time_seconds
