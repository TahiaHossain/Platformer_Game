from engine.draw import Draw
from engine.game_object import GameObject
from engine.picocore import PicoCore
from player import Player
from _platform import Platform
from enemy import *
from floor import Floor

level_layout = [
    "",
    "",
    "",
    "#####",
    "           ####     #####",
    "",
    "",
    "",
    "###############    ####"
    ]
PLATFORM_SIZE = 50
WIDTH = 700
HEIGHT = len(level_layout) * PLATFORM_SIZE

engine = PicoCore("Platformer", WIDTH, HEIGHT)

class Level(GameObject):
    def __init__(self, core, width, height, level_layout=level_layout):
        super().__init__(core, 0, 0)
        self.width = width
        self.height = height
        self.platform_width = 50
        self.platforms = []
        self.enemies = []        
        
        self.player = Player(self.core, 200, 200)
        self.enemy = EnemyOne(self.core, 200, 180)
        self.core.add_game_object(self.player)
        self.core.add_game_object(self.enemy)
        self.core.camera.follow(self.player, offset_x=self.core.width/2, offset_y=200, lerp_factor=0.1)
        
    def on_start(self):
        for i in range(len(level_layout)):
            for j in range(len(level_layout[i])):
                if level_layout[i][j] == "#":
                    x = j * self.platform_width
                    y = self.height - (i * self.platform_width)
                    
                    platform = Platform(self.core, x, y)
                    self.platforms.append(platform)
                    self.core.add_game_object(platform)

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        Draw.change_color("#FFFFFF")


# player = Player(engine, 100, 600)
# enemy = Enemy(engine, 200, 200)
# floor = Platform(engine, 0, 0)

# engine.add_game_object(player)  
# engine.add_game_object(enemy)
level = Level(engine, 700, 500)
engine.add_game_object(level)

engine.run()
