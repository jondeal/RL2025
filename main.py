import pygame
import constants
import controls
import render_display
import Game
from GameStateManager import GameStateManager
from PlayerStateManager import PlayerStateManager

pygame.init()

game = Game.Game([], None, None, None)

game.generate_new_level()

game.current_level = game.levels[0]

for tile in game.current_level.tiles:
    if tile.position == (1, 1):
        game.current_level.spawn_actor('player', tile)
    else:
        pass

player = game.current_level.actors[0]

player_state_manager = PlayerStateManager(game, player)
game_state_manager = GameStateManager(game, player)

game.game_state_manager = game_state_manager
game.player_state_manager = player_state_manager

running = True
clock = pygame.time.Clock()
FPS = constants.FPS

while running:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYUP:
            keys = pygame.key.get_pressed()
            if keys[controls.keybinds['mod key']]:
                if event.key == controls.keybinds['quit']:
                    running = False

    game.game_state_manager.current_state.update(events)

    render_display.render_display(game.current_level)

    pygame.display.flip()
