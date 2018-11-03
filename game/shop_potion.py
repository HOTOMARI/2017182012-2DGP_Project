from pico2d import*
import game_framework
import Game_Playing_Data as GPD

def enter():
    global current_time, Prevtime
    global shop_mode, sel_index
    current_time = 0
    Prevtime = 0
    shop_mode = 0
    sel_index = 0

def exit():
    pass


def update():
    global current_time, Prevtime

    current_time = get_time()

    if current_time - Prevtime > 1 / 60:
        for i in range (0,4):
            GPD.players[i].frame += 0.05
        Prevtime = current_time


def draw():
    global sel_index, shop_mode
    clear_canvas()

    # 배경 출력
    GPD.Menu.image.clip_draw(1, 1, 240, 160, 400, 300, 800, 600)

    GPD.Menu.image.clip_draw(1, 1, 240, 160, 400, 500, 800, 200)
    # 초기메뉴
    if shop_mode is 0:
        GPD.Ingame_Big_font.font.draw(100, 500, '잡화 상점입니다.',[255,255,255])

    update_canvas()


def pause(): pass


def resume(): pass


def handle_events():
    global shop_mode, sel_index

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            pass
        # a 선택 s 뒤로가기
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                # game_framework.change_state(map)
                game_framework.pop_state()
            elif event.key == SDLK_a:
                if sel_index == 0:
                    game_framework.pop_state()
                elif sel_index == 1:
                    pass
            elif event.key == SDLK_s:
                if shop_mode == 0:
                    game_framework.pop_state()