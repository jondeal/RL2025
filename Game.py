import Level


class Game:

    def __init__(self, levels, current_level, game_state_manager, player_state_manager):
        self.levels = levels
        self.current_level = current_level
        self.game_state_manager = game_state_manager
        self.player_state_manager = player_state_manager

    def generate_new_level(self):
        new_level = Level.Level([], [])
        new_level.generate_terrain()
        new_level.define_terrain()
        self.levels.append(new_level)
