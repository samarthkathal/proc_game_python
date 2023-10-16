import pygame
from os import path
import random
vec = pygame.math.Vector2



TILESIZE = 48
GRIDWIDTH = 27 # should be a multiple of 3, needed for procedural generation
GRIDHEIGHT = 15 # should be a multiple of 3, needed for procedural generation

WIDTH = TILESIZE * GRIDWIDTH
HEIGHT = TILESIZE * GRIDHEIGHT
FPS = 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FOREST = (34, 57, 10)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
DARKGRAY = (40, 40, 40)
MEDGRAY = (75, 75, 75)
LIGHTGRAY = (140, 140, 140)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#CONFIGS FOR DEBUG
icon_dir = path.join(path.dirname(__file__), 'icons')
home_img = pygame.image.load(path.join(icon_dir, 'home.png')).convert_alpha()
home_img = pygame.transform.scale(home_img, (50, 50))
#home_img.fill((0, 255, 0, 255), special_flags=pygame.BLEND_RGBA_MULT)
cross_img = pygame.image.load(path.join(icon_dir, 'player_1_1.png')).convert_alpha()
cross_img = pygame.transform.scale(cross_img, (50, 50))
#cross_img.fill((255, 0, 0, 255), special_flags=pygame.BLEND_RGBA_MULT)
wall_img = pygame.image.load(path.join(icon_dir, 'wall_1_1.png')).convert_alpha()
wall_img = pygame.transform.scale(wall_img, (50, 50))

trap_img = pygame.image.load(path.join(icon_dir, 'trap_1_1.png')).convert_alpha()
trap_img = pygame.transform.scale(trap_img, (50, 50))

arrows = {}
arrow_img = pygame.image.load(path.join(icon_dir, 'arrowRight.png')).convert_alpha()
arrow_img = pygame.transform.scale(arrow_img, (50, 50))
for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    arrows[dir] = pygame.transform.rotate(arrow_img, vec(dir).angle_to(vec(1, 0)))



move_map = {pygame.K_LEFT: pygame.Vector2(-1, 0),
            pygame.K_RIGHT: pygame.Vector2(1, 0),
            pygame.K_UP: pygame.Vector2(0, -1),
            pygame.K_DOWN: pygame.Vector2(0, 1)}


DIAGS = [vec(1,1), vec(-1,-1), vec(-1,1), vec(1,-1)]
CROSS = [vec(1, 0), vec(-1, 0), vec(0, 1), vec(0, -1)]