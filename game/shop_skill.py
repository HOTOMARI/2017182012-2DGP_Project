from pico2d import *
import game_framework
import GamePlayingData as GPD

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
    system_message = ""


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
    if shop_mode == 0:
        GPD.Ingame_Big_font.font.draw(100, 500, '스킬 상점입니다.', White_font)
        for i in range(0,4):
            if GPD.players[i].name == '전사':
                GPD.Warrior.image.clip_draw(0, 0, 72, 72, 100, 330 - 80 * i)
            elif GPD.players[i].name == '백마도사':
                GPD.WhiteMage.image.clip_draw(0, 0, 72, 72, 100, 330 - 80 * i)
            elif GPD.players[i].name == '흑마도사':
                GPD.BlackMage.image.clip_draw(0, 0, 72, 72, 100, 330 - 80 * i)
            elif GPD.players[i].name == '도적':
                GPD.Thief.image.clip_draw(0, 0, 72, 72, 100, 330 - 80 * i)

            GPD.Ingame_Big_font.font.draw(170, 330 - 80 * i, GPD.players[i].name, White_font)
            for j in range(0,4):
                GPD.Ingame_font.font.draw(275 + 100 * j, 340 - 80 * i, GPD.players[i].skill[j].name, White_font)
                GPD.Ingame_font.font.draw(275 + 100 * j, 310 - 80 * i, str(GPD.players[i].skill[j].POWER), White_font)
                pass
        GPD.Menu.image.clip_draw(242, 84, 17, 16, 50, 330 - sel_index * 80, 35, 35)  # 손가락
    # 구입메뉴
    elif shop_mode == 1:
        # 스킬 설명
        ID = GPD.players[sel_player].skill[sel_index].ID
        if ID == 1:
            GPD.Ingame_Big_font.font.draw(100, 500, '대상 적의 공격대상을 자신으로 바꿉니다.', White_font)
        elif ID == 2:
            GPD.Ingame_Big_font.font.draw(100, 500, '모든 적에게 데미지를 줍니다.', White_font)
        elif ID == 3:
            GPD.Ingame_Big_font.font.draw(100, 500, '자신에게 방어막을 씌웁니다.', White_font)
        elif ID == 4:
            GPD.Ingame_Big_font.font.draw(100, 500, '대상 적에게 큰 데미지를 줍니다.', White_font)
        elif ID == 5:
            GPD.Ingame_Big_font.font.draw(100, 500, '대상 적에게 토속성 데미지를 줍니다.', White_font)
        elif ID == 6:
            GPD.Ingame_Big_font.font.draw(100, 500, '대상 아군의 체력을 회복시킵니다.', White_font)
        elif ID == 7:
            GPD.Ingame_Big_font.font.draw(100, 500, '모든 아군의 체력을 크게 회복시킵니다.', White_font)
        elif ID == 8:
            GPD.Ingame_Big_font.font.draw(100, 500, '모든 아군에게 방어막을 씌웁니다.', White_font)
        elif ID == 9:
            GPD.Ingame_Big_font.font.draw(100, 500, '대상 적에게 빙속성 데미지를 줍니다.', White_font)
        elif ID == 10:
            GPD.Ingame_Big_font.font.draw(100, 500, '모든 적에게 화속성 데미지를 줍니다.', White_font)
        elif ID == 11:
            GPD.Ingame_Big_font.font.draw(100, 525, '자신의 체력 20%를 감소시켜', White_font)
            GPD.Ingame_Big_font.font.draw(100, 475, '마나를 회복합니다.', White_font)
        elif ID == 12:
            GPD.Ingame_Big_font.font.draw(100, 525, '자신의 현재 마나 30%를 감소시켜', White_font)
            GPD.Ingame_Big_font.font.draw(100, 475, '대상 아군의 마나를 회복시킵니다.', White_font)
        elif ID == 13:
            GPD.Ingame_Big_font.font.draw(100, 500, '대상 적에게 데미지를 줍니다.', White_font)
        elif ID == 14:
            GPD.Ingame_Big_font.font.draw(100, 500, '모든 적에게 데미지를 줍니다.', White_font)
        elif ID == 15:
            GPD.Ingame_Big_font.font.draw(100, 545, '대상 적에게 데미지를 줍니다.', White_font)
            GPD.Ingame_Big_font.font.draw(100, 495, '적의 체력이 자신의 공격력보다 낮으면', White_font)
            GPD.Ingame_Big_font.font.draw(100, 445, '추가 데미지를 줍니다.', White_font)
        elif ID == 16:
            GPD.Ingame_Big_font.font.draw(100, 500, '모든 적의 자신에 대한 적개심을 낮춥니다.', White_font)

        GPD.Ingame_Big_font.font.draw(500, 500, "남은 골드: " + str(GPD.money), White_font)

        # 스킬을 업그레이드 가능할경우 흰 글씨로 표시
        # 아니면 회색글씨로 표시
        for i in range(0,4):
            if GPD.players[sel_player].skill[i].POWER*10 <= GPD.money:
                GPD.Ingame_Big_font.font.draw(100, 330 - 70*i, GPD.players[sel_player].skill[i].name , White_font)
                GPD.Ingame_Big_font.font.draw(250, 330 - 70*i, str(GPD.players[sel_player].skill[i].POWER), [255,255,0])
                GPD.Ingame_Big_font.font.draw(550, 330 - 70*i, str(GPD.players[sel_player].skill[i].POWER * 10) + '원', White_font)
            else:
                GPD.Ingame_Big_font.font.draw(100, 330 - 70 * i, GPD.players[sel_player].skill[i].name, Gray_font)
                GPD.Ingame_Big_font.font.draw(250, 330 - 70 * i, str(GPD.players[sel_player].skill[i].POWER), [105, 105, 0])
                GPD.Ingame_Big_font.font.draw(550, 330 - 70 * i, str(GPD.players[sel_player].skill[i].POWER * 10) + '원', Gray_font)

        GPD.Menu.image.clip_draw(242, 84, 17, 16, 50, 330 - sel_index * 70, 35, 35)  # 손가락

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
            GPD.Menu.sound.play()
            if event.key == SDLK_ESCAPE:
                # game_framework.change_state(map)
                game_framework.pop_state()
            elif event.key == SDLK_a:
                if shop_mode == 0:
                    shop_mode = 1
                    sel_player = sel_index
                    sel_index = 0
                elif shop_mode == 1:
                    if GPD.players[sel_player].skill[sel_index].POWER * 10 <= GPD.money:
                        GPD.money -= GPD.players[sel_player].skill[sel_index].POWER * 10
                        GPD.players[sel_player].skill[sel_index].POWER += GPD.players[sel_player].skill[sel_index].UPGRADE
                        system_message = "업그레이드에 성공하였습니다!"
                    pass

            elif event.key == SDLK_s:
                if shop_mode == 0:
                    game_framework.pop_state()
                elif shop_mode == 1:
                    shop_mode = 0
                    sel_index = 0
                    system_message = ""
            elif event.key == SDLK_UP:
                if shop_mode == 0:
                    if sel_index > 0:
                        sel_index -= 1
                elif shop_mode == 1:
                    if sel_index > 0:
                        sel_index -= 1
            elif event.key == SDLK_DOWN:
                if shop_mode == 0:
                    if sel_index < 3:
                        sel_index += 1
                elif shop_mode == 1:
                    if sel_index < 3:
                        sel_index += 1