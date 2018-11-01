from pico2d import*
import game_framework


def enter():
    global font
    font = load_font('font\\H2SA1M.TTF')

def exit():
    global font
    del(font)
    pass

def update():
    pass

def draw():
    clear_canvas()
    font.draw(75, 115, 'GAMEOVER', [255, 255, 255])
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
