from pico2d import*
import game_framework
import Game_Playing_Data as GPD

White_font = [255,255,255]
Gray_font = [105,105,105]

def enter():
    global current_time, Prevtime
    global shop_mode, sel_index, sel_num, system_message
    current_time = 0
    Prevtime = 0
    shop_mode = 0
    sel_index = 0
    system_message = "TEST"
    sel_num = [1,1,1,1]

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
    clear_canvas()

    # 배경 출력
    GPD.Menu.image.clip_draw(1, 1, 240, 160, 400, 300, 800, 600)

    GPD.Menu.image.clip_draw(1, 1, 240, 160, 400, 500, 800, 200)
    # 초기메뉴
    if shop_mode is 0:
        GPD.Ingame_Big_font.font.draw(100, 500, '잡화 상점입니다.',White_font)
        GPD.Ingame_Big_font.font.draw(600, 500, '구입', White_font)
        GPD.Ingame_Big_font.font.draw(600, 450, '판매', White_font)
        GPD.Menu.image.clip_draw(242, 84, 17, 16, 550, 500 - sel_index * 50, 35, 35) # 손가락
    # 구입메뉴
    elif shop_mode is 1:
        # 아이템 설명
        if sel_index is 0:
            GPD.Ingame_Big_font.font.draw(100, 500, 'HP를 50 회복합니다.',White_font)
        elif sel_index is 1:
            GPD.Ingame_Big_font.font.draw(100, 500, 'MP를 50 회복합니다.',White_font)
        elif sel_index is 2:
            GPD.Ingame_Big_font.font.draw(100, 500, '모든 상태이상을 제거합니다.', White_font)
        elif sel_index is 3:
            GPD.Ingame_Big_font.font.draw(100, 475, '대상 아군의 HP와 MP를 전부 채워줍니다.', White_font)
            GPD.Ingame_Big_font.font.draw(100, 525, '대상이 죽어있었으면 부활시킵니다.', White_font)

        GPD.Ingame_Big_font.font.draw(500, 500, "남은 골드: " + str(GPD.money), White_font)
        
        # 아이템을 구입 가능할경우 흰 글씨로 표시
        # 아니면 회색글씨로 표시
        if 50 * sel_num[0] <= GPD.money:
            GPD.Ingame_Big_font.font.draw(100, 330, '포션', White_font)
            GPD.Ingame_Big_font.font.draw(250, 330, str(sel_num[0]) + '개', White_font)
            GPD.Ingame_Big_font.font.draw(550, 330, str(50 * sel_num[0]) + '원', White_font)
        else:
            GPD.Ingame_Big_font.font.draw(100, 330, '포션', Gray_font)
            GPD.Ingame_Big_font.font.draw(250, 330, str(sel_num[0]) + '개', Gray_font)
            GPD.Ingame_Big_font.font.draw(550, 330, str(50 * sel_num[0]) + '원', Gray_font)
            
        if 100 * sel_num[1] <= GPD.money:
            GPD.Ingame_Big_font.font.draw(100, 260, '에테르', White_font)
            GPD.Ingame_Big_font.font.draw(250, 260, str(sel_num[1]) + '개', White_font)
            GPD.Ingame_Big_font.font.draw(550, 260, str(100 * sel_num[1]) + '원', White_font)
        else:
            GPD.Ingame_Big_font.font.draw(100, 260, '에테르', Gray_font)
            GPD.Ingame_Big_font.font.draw(250, 260, str(sel_num[1]) + '개', Gray_font)
            GPD.Ingame_Big_font.font.draw(550, 260, str(100 * sel_num[1]) + '원', Gray_font)

        if 300 * sel_num[2] <= GPD.money:
            GPD.Ingame_Big_font.font.draw(100, 190, '만병통치약', White_font)
            GPD.Ingame_Big_font.font.draw(250, 190, str(sel_num[2]) + '개', White_font)
            GPD.Ingame_Big_font.font.draw(550, 190, str(300 * sel_num[2]) + '원', White_font)
        else:
            GPD.Ingame_Big_font.font.draw(100, 190, '만병통치약', Gray_font)
            GPD.Ingame_Big_font.font.draw(250, 190, str(sel_num[2]) + '개', Gray_font)
            GPD.Ingame_Big_font.font.draw(550, 190, str(300 * sel_num[2]) + '원', Gray_font)

        if 1000 * sel_num[3] <= GPD.money:
            GPD.Ingame_Big_font.font.draw(100, 120, '부활의 깃털', White_font)
            GPD.Ingame_Big_font.font.draw(250, 120, str(sel_num[3]) + '개', White_font)
            GPD.Ingame_Big_font.font.draw(550, 120, str(1000 * sel_num[3]) + '원', White_font)
        else:
            GPD.Ingame_Big_font.font.draw(100, 120, '부활의 깃털', Gray_font)
            GPD.Ingame_Big_font.font.draw(250, 120, str(sel_num[3]) + '개', Gray_font)
            GPD.Ingame_Big_font.font.draw(550, 120, str(1000 * sel_num[3]) + '원', Gray_font)

        GPD.Menu.image.clip_draw(242, 84, 17, 16, 50, 330 - sel_index * 70, 35, 35) #손가락

        GPD.Ingame_Big_font.font.draw(325, 50, system_message, [255,0,0])
    # 판매메뉴
    elif shop_mode is 2:
        # 아이템 설명
        if sel_index is 0:
            GPD.Ingame_Big_font.font.draw(100, 500, 'HP를 50 회복합니다.', White_font)
        elif sel_index is 1:
            GPD.Ingame_Big_font.font.draw(100, 500, 'MP를 50 회복합니다.', White_font)
        elif sel_index is 2:
            GPD.Ingame_Big_font.font.draw(100, 500, '모든 상태이상을 제거합니다.', White_font)
        elif sel_index is 3:
            GPD.Ingame_Big_font.font.draw(100, 475, '대상 아군의 HP와 MP를 전부 채워줍니다.', White_font)
            GPD.Ingame_Big_font.font.draw(100, 525, '대상이 죽어있었으면 부활시킵니다.', White_font)

        GPD.Ingame_Big_font.font.draw(500, 500, "남은 골드: " + str(GPD.money), White_font)

        # 아이템을 판매 가능할경우 흰 글씨로 표시
        # 아니면 회색글씨로 표시
        if sel_num[0] <= GPD.items[0].NUM:
            GPD.Ingame_Big_font.font.draw(100, 330, '포션', White_font)
            GPD.Ingame_Big_font.font.draw(250, 330, str(sel_num[0]) + '개', White_font)
            GPD.Ingame_Big_font.font.draw(550, 330, str(50 * sel_num[0]) + '원', White_font)
        else:
            GPD.Ingame_Big_font.font.draw(100, 330, '포션', Gray_font)
            GPD.Ingame_Big_font.font.draw(250, 330, str(sel_num[0]) + '개', Gray_font)
            GPD.Ingame_Big_font.font.draw(550, 330, str(50 * sel_num[0]) + '원', Gray_font)

        if sel_num[1] <= GPD.items[1].NUM:
            GPD.Ingame_Big_font.font.draw(100, 260, '에테르', White_font)
            GPD.Ingame_Big_font.font.draw(250, 260, str(sel_num[1]) + '개', White_font)
            GPD.Ingame_Big_font.font.draw(550, 260, str(100 * sel_num[1]) + '원', White_font)
        else:
            GPD.Ingame_Big_font.font.draw(100, 260, '에테르', Gray_font)
            GPD.Ingame_Big_font.font.draw(250, 260, str(sel_num[1]) + '개', Gray_font)
            GPD.Ingame_Big_font.font.draw(550, 260, str(100 * sel_num[1]) + '원', Gray_font)

        if sel_num[2] <= GPD.items[2].NUM:
            GPD.Ingame_Big_font.font.draw(100, 190, '만병통치약', White_font)
            GPD.Ingame_Big_font.font.draw(250, 190, str(sel_num[2]) + '개', White_font)
            GPD.Ingame_Big_font.font.draw(550, 190, str(300 * sel_num[2]) + '원', White_font)
        else:
            GPD.Ingame_Big_font.font.draw(100, 190, '만병통치약', Gray_font)
            GPD.Ingame_Big_font.font.draw(250, 190, str(sel_num[2]) + '개', Gray_font)
            GPD.Ingame_Big_font.font.draw(550, 190, str(300 * sel_num[2]) + '원', Gray_font)

        if sel_num[3] <= GPD.items[3].NUM:
            GPD.Ingame_Big_font.font.draw(100, 120, '부활의 깃털', White_font)
            GPD.Ingame_Big_font.font.draw(250, 120, str(sel_num[3]) + '개', White_font)
            GPD.Ingame_Big_font.font.draw(550, 120, str(1000 * sel_num[3]) + '원', White_font)
        else:
            GPD.Ingame_Big_font.font.draw(100, 120, '부활의 깃털', Gray_font)
            GPD.Ingame_Big_font.font.draw(250, 120, str(sel_num[3]) + '개', Gray_font)
            GPD.Ingame_Big_font.font.draw(550, 120, str(1000 * sel_num[3]) + '원', Gray_font)

        GPD.Menu.image.clip_draw(242, 84, 17, 16, 50, 330 - sel_index * 70, 35, 35)  # 손가락

        GPD.Ingame_Big_font.font.draw(325, 50, system_message, [255, 0, 0])
    update_canvas()


def pause(): pass


def resume(): pass


def handle_events():
    global shop_mode, sel_index, sel_num, system_message

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
                    if sel_index == 0:
                        shop_mode = 1
                        sel_index = 0
                    elif sel_index == 1:
                        shop_mode = 2
                        sel_index = 0
                elif shop_mode is 1:
                    if sel_index is 0:
                        if 50 * sel_num[0] <= GPD.money:
                            GPD.money -= 50 * sel_num[0]
                            GPD.items[0].NUM += sel_num[0]
                            system_message = "구매에 성공하였습니다!"
                        else:
                            system_message = "아이템이 부족합니다!"
                    elif sel_index is 1:
                        if 100 * sel_num[1] <= GPD.money:
                            GPD.money -= 100 * sel_num[1]
                            GPD.items[1].NUM += sel_num[1]
                            system_message = "구매에 성공하였습니다!"
                        else:
                            system_message = "아이템이 부족합니다!"
                    elif sel_index is 2:
                        if 300 * sel_num[2] <= GPD.money:
                            GPD.money -= 300 * sel_num[2]
                            GPD.items[2].NUM += sel_num[2]
                            system_message = "구매에 성공하였습니다!"
                        else:
                            system_message = "아이템이 부족합니다!"
                    elif sel_index is 3:
                        if 1000 * sel_num[3] <= GPD.money:
                            GPD.money -= 1000 * sel_num[3]
                            GPD.items[3].NUM += sel_num[3]
                            system_message = "구매에 성공하였습니다!"
                        else:
                            system_message = "아이템이 부족합니다!"
                elif shop_mode is 2:
                    if sel_index is 0:
                        if sel_num[0] <= GPD.items[0].NUM:
                            GPD.money += 50 * sel_num[0]
                            GPD.items[0].NUM -= sel_num[0]
                            system_message = "판매에 성공하였습니다!"
                        else:
                            system_message = "아이템이 부족합니다!"
                    elif sel_index is 1:
                        if sel_num[1] <= GPD.items[1].NUM:
                            GPD.money += 100 * sel_num[1]
                            GPD.items[1].NUM -= sel_num[1]
                            system_message = "판매에 성공하였습니다!"
                        else:
                            system_message = "아이템이 부족합니다!"
                    elif sel_index is 2:
                        if sel_num[2] <= GPD.items[2].NUM:
                            GPD.money += 300 * sel_num[2]
                            GPD.items[2].NUM -= sel_num[2]
                            system_message = "판매에 성공하였습니다!"
                        else:
                            system_message = "아이템이 부족합니다!"
                    elif sel_index is 3:
                        if sel_num[3] <= GPD.items[3].NUM:
                            GPD.money += 1000 * sel_num[3]
                            GPD.items[3].NUM -= sel_num[3]
                            system_message = "판매에 성공하였습니다!"
                        else:
                            system_message = "아이템이 부족합니다!"
            elif event.key == SDLK_s:
                if shop_mode == 0:
                    game_framework.pop_state()
                elif shop_mode is 1 or shop_mode is 2:
                    shop_mode = 0
                    sel_index = 0
                    system_message = ""
            elif event.key == SDLK_UP:
                if shop_mode is 0:
                    if sel_index > 0:
                        sel_index -= 1
                elif shop_mode is 1 or shop_mode is 2:
                    if sel_index > 0:
                        sel_index -= 1
            elif event.key == SDLK_DOWN:
                if shop_mode is 0:
                    if sel_index < 1:
                        sel_index += 1
                elif shop_mode is 1 or shop_mode is 2:
                    if sel_index < 3:
                        sel_index += 1
            elif event.key == SDLK_LEFT:
                if shop_mode is 1 or shop_mode is 2:
                    if sel_num[sel_index] > 1:
                        sel_num[sel_index] -= 1
            elif event.key == SDLK_RIGHT:
                if shop_mode is 1 or shop_mode is 2:
                    if sel_num[sel_index] < 10:
                        sel_num[sel_index] += 1