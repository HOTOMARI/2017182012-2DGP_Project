from pico2d import *
import game_framework
import Game_Playing_Data as GPD

White_font = [255, 255, 255]
Gray_font = [105, 105, 105]


def enter():
    global current_time, Prevtime
    global shop_mode, sel_index, sel_player, system_message
    current_time = 0
    Prevtime = 0
    shop_mode = 0
    sel_index = 0
    sel_player = 0
    system_message = "TEST"


def exit():
    pass


def update():
    global current_time, Prevtime

    current_time = get_time()

    if current_time - Prevtime > 1 / 60:
        for i in range(0, 4):
            GPD.players[i].frame += 0.05
        Prevtime = current_time


def draw():
    clear_canvas()

    # 배경 출력
    GPD.Menu.image.clip_draw(1, 1, 240, 160, 400, 300, 800, 600)

    GPD.Menu.image.clip_draw(1, 1, 240, 160, 400, 500, 800, 200)
    # 초기메뉴
    if shop_mode is 0:
        GPD.Ingame_Big_font.font.draw(100, 500, '일시정지 메뉴입니다.', White_font)
        GPD.Ingame_Big_font.font.draw(600, 550, '캐릭터 정보', White_font)
        GPD.Ingame_Big_font.font.draw(600, 500, '저장하기', White_font)
        GPD.Ingame_Big_font.font.draw(600, 450, '타이틀로', White_font)

        GPD.Menu.image.clip_draw(242, 84, 17, 16, 550, 550 - sel_index * 50, 35, 35)  # 손가락

    # 캐릭터 메뉴
    elif shop_mode is 1:
        for i in range(0,4):
            if GPD.players[i].name == '전사':
                GPD.Warrior.image.clip_draw(0, 0, 72, 72, 100, 330 - 80 * i)
            GPD.Ingame_Big_font.font.draw(170, 330 - 80 * i, GPD.players[i].name, White_font)
            for j in range(0,4):
                GPD.Ingame_font.font.draw(275 + 100 * j, 340 - 80 * i, GPD.players[i].skill[j].name, White_font)
                GPD.Ingame_font.font.draw(275 + 100 * j, 310 - 80 * i, str(GPD.players[i].skill[j].POWER), White_font)
        GPD.Menu.image.clip_draw(242, 84, 17, 16, 50, 330 - sel_index * 80, 35, 35)  # 손가락

        GPD.Ingame_Big_font.font.draw(325, 50, system_message, [255, 0, 0])

    update_canvas()


def pause(): pass


def resume(): pass


def handle_events():
    global shop_mode, sel_index, sel_player, system_message

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
                if shop_mode is 0:
                    if sel_index is 0:
                        shop_mode = 1
                        pass
                    elif sel_index is 1:
                        shop_mode = 2
                        pass
                    elif sel_index is 2:
                        shop_mode = 3
                        pass
                elif shop_mode is 1:
                    shop_mode = 1
                    sel_player = sel_index
                    sel_index = 0
                    pass

            elif event.key == SDLK_s:
                if shop_mode == 0:
                    game_framework.pop_state()
                elif shop_mode is 1:
                    shop_mode = 0
                    sel_index = 0
                    system_message = ""
            elif event.key == SDLK_UP:
                if shop_mode is 0:
                    if sel_index > 0:
                        sel_index -= 1
                elif shop_mode is 1:
                    if sel_index > 0:
                        sel_index -= 1
            elif event.key == SDLK_DOWN:
                if shop_mode is 0:
                    if sel_index < 2:
                        sel_index += 1
                elif shop_mode is 1:
                    if sel_index < 3:
                        sel_index += 1