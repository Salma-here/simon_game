
class Settings:

    def __init__(self):
        # screen settings
        self.screen_width = 465
        self.screen_height = 600
        self.screen_size = (self.screen_width, self.screen_height)
        self.screen_color = (200, 200, 200)  # some color

        # tile settings
        self.tile_length = 200
        self.margin = 25
        # dictionary for tile coordinates
        self.tile_coordinates = {
            1: (self.margin, 100),
            2: (self.margin + self.tile_length + 15, 100),
            3: (self.margin, 315),
            4: (self.margin + self.tile_length + 15, 315)
        }
        # dictionary for tile colors when off and normal
        self.tile_dark_colors = {
            1: (0, 0, 115),  # blue
            2: (31, 92, 0),  # green
            3: (150, 0, 0),  # red
            4: (191, 204, 4)   # yellow
        }
        # dictionary for tile colors when lighting up
        self.tile_light_colors = {
            1: (51, 92, 255),   # light blue
            2: (107, 255, 33),  # light green
            3: (255, 38, 38),   # light red
            4: (255, 251, 38)   # light yellow
        }
