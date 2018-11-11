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
    global sel_index
    GPD.Upload_data()
    background = load_image("image\\title\\background.png")
    logo = load_image("image\\title\\logo.png")
    sel_index = 0

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

    GPD.Ingame_Big_font.font.draw(340, 250, 'NEW GAME', [0, 0, 0])
    GPD.Ingame_Big_font.font.draw(340, 200, 'LOAD GAME', [0, 0, 0])
    GPD.Ingame_Big_font.font.draw(340, 150, 'HELP', [0, 0, 0])
    GPD.Ingame_Big_font.font.draw(340, 100, 'EXIT', [0, 0, 0])

    GPD.Menu.image.clip_draw(242, 84, 17, 16, 310, 250 - sel_index * 50, 35, 35)  # 손가락

    update_canvas()

def pause(): pass

def resume(): pass

def handle_events():
    global sel_index
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        # a 선택 s 뒤로가기
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_a:
                if sel_index is 0:
                    game_framework.change_state(overworld)
                elif sel_index is 1:
                    pass
                elif sel_index is 2:
                    pass
                elif sel_index is 3:
                    game_framework.quit()
            elif event.key == SDLK_UP:
                if sel_index > 0:
                    sel_index -= 1
            elif event.key == SDLK_DOWN:
                if sel_index < 3:
                    sel_index += 1