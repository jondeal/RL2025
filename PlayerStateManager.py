from PlayerStateChoosingAction import PlayerStateChoosingAction


class PlayerStateManager:
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.previous_state = None
        self.current_state = PlayerStateChoosingAction(game, player)

    def change_state(self, new_state):
        self.current_state.exit()
        self.previous_state = self.current_state
        self.current_state = new_state
        self.current_state.enter()

    def update(self, events):
        self.current_state.update(events)
