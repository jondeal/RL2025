class Actor:
    def __init__(self, name, position, rect,
                 glyph, default_glyph_color, current_glyph_color,
                 glyph_size, glyph_size_modifier, glyph_rotation,
                 dormant_glyph, dormant_glyph_color, is_dormant,
                 direction, speed, mass,
                 glo_count,
                 inventory,
                 genome,
                 action, action_item,
                 abilities,
                 turn_complete
                 ):
        self.name = name
        self.position = position
        self.rect = rect
        self.glyph = glyph
        self.default_glyph_color = default_glyph_color
        self.current_glyph_color = current_glyph_color
        self.glyph_size = glyph_size
        self.glyph_size_modifier = glyph_size_modifier
        self.glyph_rotation = glyph_rotation
        self.dormant_glyph = dormant_glyph
        self.dormant_glyph_color = dormant_glyph_color
        self.is_dormant = is_dormant
        self.direction = direction
        self.speed = speed
        self.mass = mass
        self.glo_count = glo_count
        self.inventory = inventory
        self.genome = genome
        self.action = action
        self.action_item = action_item
        self.abilities = abilities
        self.turn_complete = turn_complete

    def move(self, current_level):
        if self.name == 'player':
            for tile in current_level.tiles:
                if tile.position == (self.position[0] + self.direction[0], self.position[1] + self.direction[1]):
                    if tile.name == 'wall':
                        pass
                    else:
                        self.speed = 1
                        self.action = 'push'
                        self.turn_complete = True
        else:
            pass
