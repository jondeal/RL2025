from GameState import GameState


class GameStateAnimating(GameState):
    def __init__(self, game, player, animation_events):
        super().__init__(game)
        self.player = player
        self.animation_events = animation_events

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self, events):
        from GameStateWaitingForInput import GameStateWaitingForInput
        if self.animation_events:
            if not self.animation_events[0].is_done:
                self.animation_events[0].update()
            else:
                self.animation_events.remove(self.animation_events[0])
        else:
            self.game.game_state_manager.change_state(GameStateWaitingForInput(self.game, self.player))
