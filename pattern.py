from random import randint


class Pattern:

    def __init__(self):
        self.computer_pattern = []
        self.move_count = 0

    def initialize_pattern(self):
        self.computer_pattern = []
        self.move_count = 0

    def update_pattern(self):
        random_num = randint(1, 4)
        self.computer_pattern.append(random_num)
        print(random_num)

    def compare_patterns(self, player_move):
        if self.computer_pattern[self.move_count] == player_move:
            self.move_count += 1
            return True
        else:
            return False
