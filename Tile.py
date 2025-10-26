class Tile:
    def __init__(self, name, position, rect,
                 glyph, default_glyph_color, current_glyph_color,
                 glyph_size, glyph_size_modifier, glyph_rotation,
                 default_bg_color, current_bg_color, is_highlighted):
        self.name = name
        self.position = position
        self.rect = rect
        self.glyph = glyph
        self.default_glyph_color = default_glyph_color
        self.current_glyph_color = current_glyph_color
        self.glyph_size = glyph_size
        self.glyph_size_modifier = glyph_size_modifier
        self.glyph_rotation = glyph_rotation
        self.default_bg_color = default_bg_color
        self.current_bg_color = current_bg_color
        self.is_highlighted = is_highlighted

