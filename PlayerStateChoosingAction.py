import pygame
import controls
from PlayerState import PlayerState


class PlayerStateChoosingAction(PlayerState):
    def __init__(self, game, player):
        super().__init__(game, player)

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self, events):
        for event in events:
            #KEYDOWN instead of KEYUP makes player movement feel snappier and more responsive
            if event.type == pygame.KEYDOWN:
                if event.key == controls.keybinds['mod key']:
                    pass
                else:
                    if event.key in controls.direction_keys:
                        self.player.direction = controls.direction_keys[event.key][1]
                        self.player.move(self.game.current_level)
