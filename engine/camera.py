from engine.game_object import GameObject


class Camera:
    def __init__(self, position, zoom):
        self.position = position
        self.zoom = zoom
        self.target: GameObject = None
        self.lerp_factor = 0.1
        self.offset_x = 0
        self.offset_y = 0
        self.strict = True

    def follow(self, target, offset_x, offset_y, strict=True, lerp_factor=0.1):
        self.target = target
        self.lerp_factor = lerp_factor
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.strict = strict

    def update(self, delta_time):
        if self.target is not None:
            target_x, target_y = self.target.x, self.target.y

            if self.strict:
                target_x -= self.offset_x
                target_y -= self.offset_y
            else:
                screen_width = self.target.core.width
                if target_x + 200 > screen_width or target_x - 200 < 0:
                    return

            self.position[0] += (target_x - self.position[0]) * self.lerp_factor
            self.position[1] += (target_y - self.position[1]) * self.lerp_factor
