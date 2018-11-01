from pico2d import *
from TileMap import load_tile_map


class FixedTileBackground:

    def __init__(self):
        self.tile_map = load_tile_map('map\\overworld.json')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.tile_map.width * self.tile_map.tilewidth
        self.h = self.tile_map.height * self.tile_map.tileheight


    def set_center_object(self, boy):
        self.center_object = boy
        self.max_window_left = self.w - self.canvas_width
        self.max_window_bottom = self.h - self.canvas_height

    def draw(self):
        self.tile_map.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 0)

    def update(self):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width//2, self.max_window_left)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height//2, self.max_window_bottom)