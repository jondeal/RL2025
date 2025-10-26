import bools
import pygame.freetype
import os

pygame.freetype.init()
pygame.display.init()
pygame.display.set_caption('RL2025')
pygame.mouse.set_visible(False)

FPS = 60

PHI = 1.618

screen_info = pygame.display.Info()

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (screen_info.current_w - screen_info.current_h, 0)

if bools.is_fullscreen:
    screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.NOFRAME)

level_surface = pygame.Surface((screen_info.current_w // PHI, screen_info.current_h))
message_surface = pygame.Surface((screen_info.current_w - (screen_info.current_w // PHI), screen_info.current_h))

LEVEL_SIZE = (40, 40)
CHUNK_SIZE = (20, 20)

TILE_WIDTH = level_surface.get_width() // CHUNK_SIZE[0]
TILE_HEIGHT = level_surface.get_height() // CHUNK_SIZE[1]

FONT_SIZE = TILE_WIDTH

FONT = pygame.freetype.Font('/usr/share/fonts/truetype/julia/JuliaMono-Light.ttf', FONT_SIZE)
