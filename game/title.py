from pico2d import*
import Game_Playing_Data as GPD
import game_framework
import overworld
import dungeon
import town

background = None
logo = None
time = 0

def enter():
    global background, logo
    GPD.Upload_data()
    background = load_image("image\\title\\background.png")
    logo = load_image("image\\title\\logo.png")

def exit():
    pass

def update():
    global time
    time = get_time()

def draw():
    global background, logo
    clear_canvas()
    background.clip_draw(0,0,1,1,400,300,800,600)
    logo.clip_draw(0,0,509,120,400,400)
    if time % 1 > 0.5:
        GPD.Ingame_Big_font.font.draw(270, 200, 'PRESS ANY KEY TO START', [0, 0, 0])
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
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            else:
                pass