from GameState import GameState
import physics


class GameStateResolvingPhysics(GameState):
    def __init__(self, game, player):
        super().__init__(game)
        self.player = player

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self, events):
        from GameStateAnimating import GameStateAnimating
        if physics.resolve_physics(self.game.current_level) is True:
            self.game.game_state_manager.change_state(GameStateAnimating(self.game,
                                                                         self.player,
                                                                         physics.animation_events))
        else:
            pass
