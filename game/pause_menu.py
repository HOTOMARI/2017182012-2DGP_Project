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
    # 능력치 증가 테스트용
    GPD.players[0].AP += 5


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
        GPD.Ingame_Big_font.font.draw(100, 500, '캐릭터의 능력치를 상승시킬 수 있습니다.', White_font)
        for i in range(0,4):
            if GPD.players[i].name == '전사':
                GPD.Warrior.image.clip_draw(0, 0, 72, 72, 100, 330 - 80 * i)
            GPD.Ingame_Big_font.font.draw(170, 330 - 80 * i, GPD.players[i].name, White_font)

            GPD.Ingame_font.font.draw(275, 340 - 80 * i, 'HP', White_font)
            GPD.Ingame_font.font.draw(275, 310 - 80 * i, str(GPD.players[i].HP) + '/' + str(GPD.players[i].MAX_HP),
                                      White_font)

            GPD.Ingame_font.font.draw(350, 340 - 80 * i, 'MP', White_font)
            GPD.Ingame_font.font.draw(350, 310 - 80 * i, str(GPD.players[i].MP) + '/' + str(GPD.players[i].MAX_MP),
                                      White_font)

            GPD.Ingame_font.font.draw(425, 340 - 80 * i, 'EXP', White_font)
            GPD.Ingame_font.font.draw(425, 310 - 80 * i, str(GPD.players[i].EXP) + '/' + str(GPD.players[i].MAX_EXP),
                                      White_font)

            GPD.Ingame_font.font.draw(500, 340 - 80 * i, 'ATK', White_font)
            GPD.Ingame_font.font.draw(500, 310 - 80 * i, str(GPD.players[i].ATK), White_font)

            GPD.Ingame_font.font.draw(575, 340 - 80 * i, 'DEF', White_font)
            GPD.Ingame_font.font.draw(575, 310 - 80 * i, str(GPD.players[i].DEF), White_font)

            GPD.Ingame_font.font.draw(650, 340 - 80 * i, 'AP', White_font)
            GPD.Ingame_font.font.draw(650, 310 - 80 * i, str(GPD.players[i].AP),  White_font)

        GPD.Menu.image.clip_draw(242, 84, 17, 16, 50, 330 - sel_index * 80, 35, 35)  # 손가락
    elif shop_mode is 4:
        GPD.Ingame_Big_font.font.draw(100, 330, 'MAX HP', White_font)
        GPD.Ingame_Big_font.font.draw(250, 330, str(GPD.players[sel_player].MAX_HP), [255,0,0])

        GPD.Ingame_Big_font.font.draw(100, 260, 'MAX MP', White_font)
        GPD.Ingame_Big_font.font.draw(250, 260, str(GPD.players[sel_player].MAX_MP), [0, 255, 255])

        GPD.Ingame_Big_font.font.draw(100, 190, 'ATK', White_font)
        GPD.Ingame_Big_font.font.draw(250, 190, str(GPD.players[sel_player].ATK), [255, 255, 0])

        GPD.Ingame_Big_font.font.draw(100, 120, 'DEF', White_font)
        GPD.Ingame_Big_font.font.draw(250, 120, str(GPD.players[sel_player].DEF), [0, 255, 0])

        GPD.Ingame_Big_font.font.draw(550, 270, '남은 AP', White_font)
        GPD.Ingame_Big_font.font.draw(570, 220, str(GPD.players[sel_player].AP), White_font)

        GPD.Menu.image.clip_draw(242, 84, 17, 16, 50, 330 - sel_index * 70, 35, 35)  # 손가락
        pass
    # 저장메뉴
    elif shop_mode is 2:
        GPD.Ingame_Big_font.font.draw(100, 500, '데이터를 저장하시겠습니까?', White_font)
        GPD.Ingame_Big_font.font.draw(600, 500, '네', White_font)
        GPD.Ingame_Big_font.font.draw(600, 450, '아니오', White_font)
        GPD.Menu.image.clip_draw(242, 84, 17, 16, 550, 500 - sel_index * 50, 35, 35)  # 손가락
        pass
    # 타이틀로
    elif shop_mode is 3:
        pass

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
                    shop_mode = 4
                    sel_player = sel_index
                    sel_index = 0
                    pass
                elif shop_mode is 4:
                    if GPD.players[sel_player].AP > 0:
                        if sel_index is 0:
                            GPD.players[sel_player].MAX_HP += 3
                            GPD.players[sel_player].AP -= 1
                            pass
                        elif sel_index is 1:
                            GPD.players[sel_player].MAX_MP += 2
                            GPD.players[sel_player].AP -= 1
                            pass
                        elif sel_index is 2:
                            GPD.players[sel_player].ATK += 1
                            GPD.players[sel_player].AP -= 1
                            pass
                        elif sel_index is 3:
                            GPD.players[sel_player].DEF += 1
                            GPD.players[sel_player].AP -= 1
                            pass
                    pass
                elif shop_mode is 2:
                    if sel_index is 0:
                        pass
                    elif sel_index is 1:
                        shop_mode = 0
                        sel_index = 0
                        pass
                    pass
                elif shop_mode is 3:
                    pass

            elif event.key == SDLK_s:
                if shop_mode == 0:
                    game_framework.pop_state()
                elif shop_mode is 4:
                    shop_mode = 1
                else:
                    shop_mode = 0
                    sel_index = 0
                    system_message = ""
            elif event.key == SDLK_UP:
                    if sel_index > 0:
                        sel_index -= 1
            elif event.key == SDLK_DOWN:
                if shop_mode is 0:
                    if sel_index < 2:
                        sel_index += 1
                elif shop_mode is 1 or shop_mode is 4:
                    if sel_index < 3:
                        sel_index += 1
                elif shop_mode is 2:
                    if sel_index < 1:
                        sel_index += 1