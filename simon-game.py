# courtesy of Salma ye Erfani (also Negin Mehrdad)

#sound
#text
#game over
#play button
#file

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

        self.tiles = [Tile(self, i) for i in range(0, 4)]
        self.pattern = Pattern(self)
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
            elif event.type==pygame.MOUSEBUTTONDOWN:
                tile_num=self.pattern.compare_patterns(pygame.mouse.get_pos())
                self.pattern.move_count+=1
                if tile_num==-1:
                    self.run=False
                    print('You lose sucker!!!')
                else:
                    self.tiles[tile_num].toggle_color()
                    self._update_screen()
            elif event.type==pygame.MOUSEBUTTONUP:
                tile_num=self.pattern.computer_pattern[self.pattern.move_count-1]
                self.tiles[tile_num].toggle_color()
                self._update_screen()


    def _color_toggle(self,num):
        self.tiles[num].toggle_color()   # light tile up 
        self._update_screen()
        sleep(0.5)
        self.tiles[num].toggle_color()   # return tile color to normal
        self._update_screen()
        sleep(0.5)


    def _update_screen(self):
        self.screen.fill(self.settings.screen_color)
        for tile in self.tiles:
            tile.draw_tile()
        pygame.display.flip()

    def show_pattern(self):
        for number in self.pattern.computer_pattern:
            self._color_toggle(number)  


if __name__ == '__main__':
    simon_game = SimonGame()
    simon_game.run_game()
