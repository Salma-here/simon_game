
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
            0: (self.margin, 100),
            1: (self.margin + self.tile_length + 15, 100),
            2: (self.margin, 315),
            3: (self.margin + self.tile_length + 15, 315)
        }
        # dictionary for tile colors when off and normal
        self.tile_dark_colors = {
            0: (0, 0, 115),  # blue
            1: (31, 92, 0),  # green
            2: (150, 0, 0),  # red
            3: (191, 204, 4)   # yellow
        }
        # dictionary for tile colors when lighting up
        self.tile_light_colors = {
            0: (0, 0, 230),   # light blue
            1: (62, 184, 0),  # light green
            2: (255, 0, 0),   # light red
            3: (255, 255, 8)   # light yellow
        }


