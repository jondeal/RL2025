import constants
import render_level


def render_display(level):
    constants.screen.fill('PURPLE')  #DEBUG
    constants.level_surface.fill('ORANGE')  #DEBUG
    constants.message_surface.fill([0, 0, 30])
    render_level.render_level(level)
    constants.screen.blit(constants.level_surface, constants.screen.get_rect())
    constants.screen.blit(constants.message_surface, (constants.level_surface.get_width(), 0))
