from pico2d import*
from math import*
import random


Diagonal = sqrt(3)

# Character Event
RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP = range(8)

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

class RunState:
    @staticmethod
    def enter(character):
        character.frame = 0

    @staticmethod
    def exit(character):
        pass

    @staticmethod
    def do(character):
        character.frame += 1 / 30
        if character.move_dir[0] and character.move_dir[1] == 0 and character.move_dir[2] == 0 and character.move_dir[3] == 0:
            character.state = 3
            character.x -= 3
            character.play_lotto(100)
        elif character.move_dir[1] and character.move_dir[0] == 0 and character.move_dir[2] == 0 and character.move_dir[3] == 0:
            character.state = 2
            character.x += 3
            character.play_lotto(100)
        elif character.move_dir[2] and character.move_dir[1] == 0 and character.move_dir[0] == 0 and character.move_dir[3] == 0:
            character.state = 1
            character.y += 3
            character.play_lotto(100)
        elif character.move_dir[3] and character.move_dir[1] == 0 and character.move_dir[2] == 0 and character.move_dir[0] == 0:
            character.state = 0
            character.y -= 3
            character.play_lotto(100)

        elif character.move_dir[0] and character.move_dir[2]:
            character.state = 1
            character.x -= Diagonal
            character.y += Diagonal
            character.play_lotto(100)
        elif character.move_dir[1] and character.move_dir[2]:
            character.state = 1
            character.x += Diagonal
            character.y += Diagonal
            character.play_lotto(100)
        elif character.move_dir[0] and character.move_dir[3]:
            character.state = 0
            character.x -= Diagonal
            character.y -= Diagonal
            character.play_lotto(100)
        elif character.move_dir[1] and character.move_dir[3]:
            character.state = 0
            character.x += Diagonal
            character.y -= Diagonal
            character.play_lotto(100)

        character.x = clamp(0, character.x, character.bg.w)
        character.y = clamp(0, character.y, character.bg.h)

    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frame % 2) * 36 + 72 * character.state, 396, 36, 36,
                                  character.x - character.bg.window_left, character.y - character.bg.window_bottom)


next_state_table = {
    RunState:{RIGHT_UP: RunState, LEFT_UP: RunState,
               RIGHT_DOWN:RunState, LEFT_DOWN: RunState,
               UP_UP: RunState, DOWN_UP: RunState,
               UP_DOWN: RunState, DOWN_DOWN: RunState},
}



class Character():

    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 32
        self.height = 32
        self.frame = 0
        self.move_dir=[0,0,0,0]
        self.state = 0
        self.battle_start = False
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()

        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self)

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
            self.change_state(next_state_table[self.cur_state][event])

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
            if key_event == RIGHT_DOWN:
                self.move_dir[1] = 1
            elif key_event == LEFT_DOWN:
                self.move_dir[0] = 1
            elif key_event == UP_DOWN:
                self.move_dir[2] = 1
            elif key_event == DOWN_DOWN:
                self.move_dir[3] = 1

            elif key_event == RIGHT_UP:
                self.move_dir[1] = 0
            elif key_event == LEFT_UP:
                self.move_dir[0] = 0
            elif key_event == UP_UP:
                self.move_dir[2] = 0
            elif key_event == DOWN_UP:
                self.move_dir[3] = 0
            self.add_event(key_event)

    def play_lotto(self,mother):
        # 1/mother의 확률로 배틀 들어감
        if random.randint(0,mother) is 0:
            self.battle_start = True