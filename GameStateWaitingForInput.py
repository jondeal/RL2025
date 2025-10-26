from GameState import GameState
from GameStateResolvingPhysics import GameStateResolvingPhysics


class GameStateWaitingForInput(GameState):
    def __init__(self, game, player):
        super().__init__(game)
        self.player = player

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self, events):
        if self.player.turn_complete is False:
            self.game.player_state_manager.update(events)
        else:
            self.player.turn_complete = False
            self.game.game_state_manager.change_state(GameStateWaitingForInput)
            self.game.game_state_manager.change_state(GameStateResolvingPhysics(self.game, self.player))
