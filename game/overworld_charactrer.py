import game_framework
from pico2d import*
from math import*
import random


Diagonal = sqrt(3)

# Character Event
RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP, NO_KEYS = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP
}


# Character States

class IdleState:
    @staticmethod
    def enter(character, event):
        if event == RIGHT_DOWN:
            character.x_velocity += 32 * 10
        elif event == LEFT_DOWN:
            character.x_velocity -= 32 * 10
        elif event == RIGHT_UP:
            character.x_velocity -= 32 * 10
        elif event == LEFT_UP:
            character.x_velocity += 32 * 10

        if event == UP_DOWN:
            character.y_velocity += 32 * 10
        elif event == DOWN_DOWN:
            character.y_velocity -= 32 * 10
        elif event == UP_UP:
            character.y_velocity -= 32 * 10
        elif event == DOWN_UP:
            character.y_velocity += 32 * 10

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        character.frame += 6 * game_framework.frame_time

    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frame % 2) * 36 + 72 * character.state, 396, 36, 36,
                                  character.x - character.bg.window_left, character.y - character.bg.window_bottom)

class RunState:
    @staticmethod
    def enter(character, event):
        if event == RIGHT_DOWN:
            character.x_velocity += 32*10
        elif event == LEFT_DOWN:
            character.x_velocity -= 32*10
        elif event == RIGHT_UP:
            character.x_velocity -= 32*10
        elif event == LEFT_UP:
            character.x_velocity += 32*10

        if event == UP_DOWN:
            character.y_velocity += 32*10
        elif event == DOWN_DOWN:
            character.y_velocity -= 32*10
        elif event == UP_UP:
            character.y_velocity -= 32*10
        elif event == DOWN_UP:
            character.y_velocity += 32*10

        if character.x_velocity is 0 and character.y_velocity is 0:
            character.add_event(NO_KEYS)

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        character.frame += 6*game_framework.frame_time

        character.x += character.x_velocity * game_framework.frame_time
        character.y += character.y_velocity * game_framework.frame_time

        character.x = clamp(0, character.x, character.bg.w)
        character.y = clamp(0, character.y, character.bg.h)

    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frame % 2) * 36 + 72 * character.state, 396, 36, 36,
                                  character.x - character.bg.window_left, character.y - character.bg.window_bottom)


next_state_table = {
    RunState:{RIGHT_UP: RunState, LEFT_UP: RunState,
               RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
               UP_UP: RunState, DOWN_UP: RunState,
               UP_DOWN: RunState, DOWN_DOWN: RunState,
               NO_KEYS: IdleState},

    IdleState:{RIGHT_UP: RunState, LEFT_UP: RunState,
               RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
               UP_UP: RunState, DOWN_UP: RunState,
               UP_DOWN: RunState, DOWN_DOWN: RunState}
}



class Character():

    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 32
        self.height = 32
        self.frame = 0
        self.x_velocity = 0
        self.y_velocity = 0
        self.state = 0
        self.battle_start = False
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

        if Character.image == None:
            Character.image = load_image('image\\overworld_characters.png')

    def change_state(self,  state):
        self.cur_state.exit(self)
        self.cur_state = state
        self.cur_state.enter(self)

    def add_event(self, event):
       self.event_que.insert(0, event)

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def draw_bb(self):
        draw_rectangle(self.get_bb()[0] - self.bg.window_left,
                       self.get_bb()[1] - self.bg.window_bottom,
                       self.get_bb()[2] - self.bg.window_left,
                       self.get_bb()[3] - self.bg.window_bottom)

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def play_lotto(self,mother):
        # 1/mother의 확률로 배틀 들어감
        if random.randint(0,mother) is 0:
            self.battle_start = True