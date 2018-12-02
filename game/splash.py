from pico2d import*
import GamePlayingData as GPD
import game_framework
import title

background = None
time = 0


def enter():
    global background
    background = load_image("image\\title\\background.png")


def exit():
    GPD.Upload_data()


def update():
    global time
    time += game_framework.frame_time
    if time > 1:
        game_framework.change_state(title)


def draw():
    clear_canvas()
    background.clip_draw(0,0,1,1,400,300,800,600)

    update_canvas()


def pause():
    pass


def resume():
    pass


def handle_events():
    pass
