# courtesy of Salma ye Erfani (also Negin Mehrdad)
from time import sleep

import pygame

from pattern import Pattern
from settings import Settings
from tile import Tile


class SimonGame:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_caption('A game of simon!!!')

        self.tiles = [Tile(self, i) for i in range(1, 5)]
        self.pattern = Pattern()
        self.run = True

    def run_game(self):
        while self.run:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.run = False
                elif event.key == pygame.K_SPACE:
                    self.pattern.update_pattern()
                    self.show_pattern()

    def _update_screen(self):
        self.screen.fill(self.settings.screen_color)
        for tile in self.tiles:
            tile.draw_tile()
        pygame.display.flip()

    def show_pattern(self):
        for number in self.pattern.computer_pattern:
            number -= 1
            print('number is', number)
            self.tiles[number].toggle_color()  # light tile up
            self._update_screen()
            sleep(1)
            self.tiles[number].toggle_color()  # return tile color to normal
            self._update_screen()


if __name__ == '__main__':
    simon_game = SimonGame()
    simon_game.run_game()
