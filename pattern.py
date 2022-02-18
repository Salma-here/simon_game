from random import randint


class Pattern:

    def __init__(self,simon_game):
        self.computer_pattern = []
        self.tiles=simon_game.tiles
        self.move_count = 0

    def initialize_pattern(self):
        self.computer_pattern = []
        self.move_count = 0

    def update_pattern(self):
        self.move_count=0
        random_num = randint(0, 3)
        self.computer_pattern.append(random_num)

    def compare_patterns(self, pos):
        tile_num=self.computer_pattern[self.move_count]
        if self.tiles[tile_num].rect.collidepoint(pos):
            return tile_num
        else:
            return -1


