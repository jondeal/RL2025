import constants
import pygame

bg_surface = pygame.Surface((constants.TILE_WIDTH, constants.TILE_HEIGHT))

def render_level(level):

    for tile in level.tiles:
        if tile.is_highlighted:
            tile.current_bg_color = [100, 100, 0, 255]
        else:
            tile.current_bg_color = tile.default_bg_color
        bg_surface.fill(tile.current_bg_color)
        constants.level_surface.blit(bg_surface, tile.rect)
        tile.current_glyph_color[3] = 255
        for actor in level.actors:
            if actor.rect == tile.rect:
                tile.current_glyph_color = [tile.current_glyph_color[0], tile.current_glyph_color[1], tile.current_glyph_color[2], 0]

    to_render = [level.tiles, level.actors]

    for entity_list in to_render:
        for entity in entity_list:
            if entity.glyph_size != constants.FONT_SIZE:
                size = entity.glyph_size
            else:
                size = constants.FONT_SIZE * entity.glyph_size_modifier
            if entity in level.actors and entity.is_dormant:
                glyph = entity.dormant_glyph
                glyph_color = entity.dormant_glyph_color
            else:
                glyph = entity.glyph
                glyph_color = entity.current_glyph_color

            glyph_image, glyph_rect = constants.FONT.render(glyph, glyph_color, None, size=size,
                                                            rotation=entity.glyph_rotation)

            glyph_rect.center = entity.rect.center

            constants.level_surface.blit(glyph_image, glyph_rect)
