from pico2d import*
import game_framework
import Game_Playing_Data
import battle


def enter():
    global background, menu,font
    global current_time, Prevtime
    global message_index
    global total_money, total_exp
    #open_canvas()
    background = battle.background
    current_time = 0
    Prevtime = 0
    message_index = 0

    for i in range(0, 4):
        if Game_Playing_Data.players[i].act_type != 7:
            Game_Playing_Data.players[i].act_type = 4

    total_money = 0
    total_exp = 0
    for i in range(0, 3):
        total_money += Game_Playing_Data.monsters[i].MONEY
        total_exp += Game_Playing_Data.monsters[i].EXP



def exit():
    for i in range(0, 4):
        Game_Playing_Data.players[i].act_type = 0


def update():
    global current_time, Prevtime

    current_time = get_time()

    if current_time - Prevtime > 1 / 60:
        for i in range (0,4):
            Game_Playing_Data.players[i].frame += 0.05
        Prevtime = current_time


def draw():
    global backgound
    global message_index
    clear_canvas()

    # 배경 출력
    background.clip_draw(0, 0, 1000, 740, 400, 400, 800, 500)

    # 플레이어 출력
    for i in range(0, 4):
        Game_Playing_Data.players[i].draw()

    # 하단 메뉴 출력
    Game_Playing_Data.Menu.image.clip_draw(0, 0, 240, 160, 400, 75, 800, 150)

    if message_index == 0:
        Game_Playing_Data.Ingame_font.font.draw(360, 75, '전투 승리', [255, 255, 255])
    elif message_index == 1:
        Game_Playing_Data.Ingame_font.font.draw(300, 75, '골드 ' + str(total_money) + '를 획득하였습니다.', [255, 255, 255])
    elif message_index == 2:
        Game_Playing_Data.Ingame_font.font.draw(300, 75, '경험치 ' + str(total_exp) + '를 획득하였습니다.', [255, 255, 255])

    update_canvas()


def pause(): pass


def resume(): pass


def handle_events():
    global message_index

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
                if message_index == 2:
                    game_framework.pop_state()
                message_index += 1