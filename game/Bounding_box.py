from pico2d import *

class BaseZone:
    def __init__(self, zone_data, base_height):
        self.width, self.height = zone_data['width'], zone_data['height']
        self.x, self.y = zone_data['x'] + self.width / 2, base_height - (zone_data['y'] + self.height / 2)


    def set_background(self, background):
        self.background = background

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def draw_bb(self, background):
        draw_rectangle(self.get_bb()[0] - background.window_left,
                       self.get_bb()[1] - background.window_bottom,
                       self.get_bb()[2] - background.window_left,
                       self.get_bb()[3] - background.window_bottom)
