import pygame


class Tile:
    def __init__(self, simon_game, tile_num):
        self.screen = simon_game.screen
        self.screen_rect = simon_game.screen.get_rect()
        self.settings = simon_game.settings
        self.tile_num = tile_num
        self.color = self.settings.tile_dark_colors[self.tile_num]
        self.coordinates = self.settings.tile_coordinates[self.tile_num]
        self.rect = pygame.Rect(self.coordinates[0], self.coordinates[1], self.settings.tile_length, self.settings.tile_length)

    def draw_tile(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def toggle_color(self):
        if self.color in self.settings.tile_dark_colors.values():
            self.color = self.settings.tile_light_colors[self.tile_num]
        else:
            self.color = self.settings.tile_dark_colors[self.tile_num]
    

