from pico2d import*
import game_framework
import GamePlayingData as GPD
import title

background = None

def enter():
    global background
    if background is None:
        background = load_image('image\\black_point.png')
    GPD.Upload_data()

def exit():
    pass

def update():
    pass

def draw():
    clear_canvas()
    background.clip_draw(0, 0, 1, 1, 400, 300, 800, 600)
    GPD.Ingame_Big_font.font.draw(325, 300, 'GAME OVER', [255, 0, 0])
    update_canvas()

def pause(): pass

def resume(): pass

def handle_events():
    global dirx, diry, dir
    global frame, moving
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            game_framework.change_state(title)
