import random
import pygame

import constants
import controls

import Tile
import Actor

import tile_templates
import actor_templates


class Level:
    def __init__(self, tiles, actors):
        self.tiles = tiles
        self.actors = actors

    def get_points(self, start_point, end_point):
        points = []
        if end_point is not None:
            n = max(abs(end_point[0] - start_point[0]), abs(end_point[1] - start_point[1]))
            step = 0
            while step <= n:
                if n == 0:
                    t = 0
                else:
                    t = step / n

                point = (round(start_point[0] + t * (end_point[0] - start_point[0])),
                         round(start_point[1] + t * (end_point[1] - start_point[1])))
                points.append(point)
                step += 1

        return points

    def get_random_open_tile(self):
        open_tiles = []
        for tile in self.tiles:
            if tile.name != 'wall':
                open_tiles.append(tile)
            for actor in self.actors:
                if actor.position == tile.position:
                    open_tiles.remove(tile)
        if open_tiles:
            random_open_tile = random.choice(open_tiles)
            return random_open_tile
        else:
            print('Error: no open tiles')
            pass

    def get_random_open_neighboring_tile(self, entity):
        direction_list = [direction[1] for direction in controls.direction_keys.values()]
        tiles_dict = {tile.position: tile for tile in self.tiles}
        neighboring_tiles = []
        open_neighboring_tiles = []
        for direction in direction_list:
            desired_position = (entity.position[0] + direction[0], entity.position[1] + direction[1])
            if desired_position in tiles_dict:
                neighboring_tiles.append(tiles_dict[desired_position])
        for tile in neighboring_tiles:
            if tile.name != 'wall':
                open_neighboring_tiles.append(tile)
            else:
                pass
        if open_neighboring_tiles:
            return random.choice(open_neighboring_tiles)
        else:
            print(f'{entity.name}: no valid choice for open neighboring tile; defaulting to own position')
            for tile in self.tiles:
                if tile.position == entity.position:
                    return tile

    def generate_terrain(self):
        # generates a grid of floor tiles
        for i in range(constants.LEVEL_SIZE[0]):
            x = i
            for i_2 in range(constants.LEVEL_SIZE[1]):
                y = i_2

                tile_rect = pygame.Rect(constants.level_surface.get_rect().left + x * constants.TILE_WIDTH,
                                        constants.level_surface.get_rect().top + y * constants.TILE_HEIGHT,
                                        constants.TILE_WIDTH,
                                        constants.TILE_HEIGHT)

                new_tile = Tile.Tile('floor', (x, y), tile_rect,
                                     None, None, None,
                                     constants.FONT_SIZE, None, 0,
                                     None, None, False)

                self.tiles.append(new_tile)
        # this makes border walls
        for tile in self.tiles:
            if (tile.position[0] == 0 or tile.position[0] == constants.LEVEL_SIZE[0] - 1
                    or tile.position[1] == 0 or tile.position[1] == constants.LEVEL_SIZE[1] - 1):
                tile.name = 'wall'

    def define_terrain(self):
        for tile in self.tiles:
            for template in tile_templates.tile_templates:
                if template['name'] == tile.name:
                    tile.glyph = template['glyph']
                    tile.default_glyph_color = template['default_glyph_color']
                    tile.current_glyph_color = template['default_glyph_color']
                    tile.glyph_size_modifier = template['glyph_size_modifier']
                    tile.default_bg_color = (
                        template['bg_base_rgba'][0] + random.randrange(template['bg_rgb_range'][0][0], template['bg_rgb_range'][0][1]),
                        template['bg_base_rgba'][1] + random.randrange(template['bg_rgb_range'][1][0], template['bg_rgb_range'][1][1]),
                        template['bg_base_rgba'][2] + random.randrange(template['bg_rgb_range'][2][0], template['bg_rgb_range'][2][1]),
                        template['bg_base_rgba'][3]
                    )

    def spawn_actor(self, actor_type, destination):
        for template in actor_templates.actor_templates:
            if template['name'] == actor_type:
                new_actor = Actor.Actor(template['name'],
                                        destination.position, destination.rect.copy(),
                                        template['glyph'],
                                        template['default_glyph_color'], template['default_glyph_color'],
                                        constants.FONT_SIZE, template['glyph_size_modifier'], 0,
                                        template['dormant_glyph'], template['dormant_glyph_color'], True,
                                        (0, 0), 0, template['mass'],
                                        template['glo_count'],
                                        [],
                                        [],
                                        None, None,
                                        [],
                                        False
                                        )

                self.actors.append(new_actor)

    def spawn_terrain(self, terrain_name, limit):
        terrain_count = 0

        # turns random unblocked tiles into a given terrain type
        while terrain_count < limit:
            random_tile = self.get_random_open_tile()
            for template in tile_templates.tile_templates:
                if template['name'] == terrain_name:
                    random_tile.name = template['name']
            terrain_count += 1
