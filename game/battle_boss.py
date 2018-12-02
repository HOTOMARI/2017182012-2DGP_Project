from pico2d import *
import game_framework
import GamePlayingData as GPD
import random
import gameover
import battle_win

Battle_is_End = False
background = None
background_final = None
Phase_Change = False
BattlelogBack = None


def enter():
    global current_time, Prevtime
    global background, background_final, turn_image, BattlelogBack
    global sel_menu_type, sel_menu_mode, menu_index, turn_queue, player_turn_index, monster_turn_index, monster_NO_deadshot
    global turn_end_sign, monster_turn_sign, monster_turn_step, turn_queue_index, animation_end, timer
    global Phase_Change
    # open_canvas()
    current_time = 0
    Prevtime = 0

    while len(GPD.Battlelog) != 0:
        GPD.Battlelog.pop()

    background = load_image('image\\battlebacks\\Boss.png')
    background_final = load_image('image\\battlebacks\\Boss_Final.png')

    turn_image = load_image('image\\player\\select.png')
    BattlelogBack = load_image('image\\battlelog.png')

    GPD.bgm.firstboss.repeat_play()

    # 0 1차메뉴 1 2차메뉴 2 3차메뉴-1 3 3차메뉴-2
    sel_menu_type = 0
    # 0 None 1 attack 2 skill 3 item
    sel_menu_mode = 0
    menu_index = [0, 0, 0, 0]

    # 플레이어누구 조종하는지
    player_turn_index = 0
    monster_turn_index = 0

    # 앞의 플레이어가 죽었을 경우 턴 넘김
    for i in range(0, 4):
        if GPD.players[i].act_type == 7:
            player_turn_index += 1
        else:
            break

    # 액션종류
    # 1 attack  num1 누가 num2 누구를
    # skill
    # 2-type1   num1 누가 num2 무슨스킬을  - 자신에게 적용 & 적 전체에 적용 & 우리편 전체에 적용
    # 3-type2   num1 누가 num2 무슨스킬을  num3 누구에게  - 우리편중 하나에 적용 & 적 하나에 적용
    # 4 item    num1 누가 num2 무슨아이템을 num3 누구에게
    turn_queue = []
    turn_end_sign = False
    monster_turn_sign = False
    monster_turn_step = 0
    turn_queue_index = 0
    animation_end = False
    monster_NO_deadshot = False
    timer = 0
    Phase_Change = False


def exit():
    global background, turn_image
    del (background)
    del (turn_image)

    GPD.monsters.pop()


def update():
    global Battle_is_End
    global turn_queue, turn_queue_index, turn_end_sign, player_turn_index, animation_end
    global monster_turn_sign, monster_turn_index, monster_turn_step, monster_NO_deadshot
    global current_time, Prevtime
    global Phase_Change

    current_time = get_time()

    if current_time - Prevtime > 1 / 60:

        if Battle_is_End:
            Battle_is_End = False
            game_framework.pop_state()
        elif Phase_Change is True:
            GPD.monsters[0].phase = 1
            GPD.monsters[0].act_type = 2
            GPD.monsters[0].next_skill = 0

            GPD.bgm.secondboss.repeat_play()
            Phase_Change = False
            turn_end_sign = False
            monster_turn_sign = False
            pass
        else:
            for i in range(0, 4):
                GPD.players[i].renew_status()
                GPD.players[i].frame += game_framework.frame_time * 45
            GPD.monsters[0].frame += game_framework.frame_time * 45

            if turn_end_sign and len(turn_queue) != 0:
                do_player_animation()
                # 플레이어 평타
                if animation_end:
                    if turn_queue[0][0] == 1:
                        GPD.players[turn_queue[0][1]].attack(turn_queue[0][1], turn_queue[0][2])
                        turn_queue.remove([turn_queue[0][0], turn_queue[0][1], turn_queue[0][2]])
                        animation_end = False
                    # 플레이어 스킬사용
                    elif turn_queue[0][0] == 2:
                        GPD.players[turn_queue[0][1]].skill[turn_queue[0][2]].activate(turn_queue[0][1])
                        turn_queue.remove([turn_queue[0][0], turn_queue[0][1], turn_queue[0][2]])
                        animation_end = False
                    elif turn_queue[0][0] == 3:
                        GPD.players[turn_queue[0][1]].skill[turn_queue[0][2]].activate(turn_queue[0][1],
                                                                                       turn_queue[0][3])
                        turn_queue.remove([turn_queue[0][0], turn_queue[0][1], turn_queue[0][2], turn_queue[0][3]])
                        animation_end = False
                    # 플레이어 아이템 사용
                    elif turn_queue[0][0] == 4:
                        GPD.items[turn_queue[0][2]].use(turn_queue[0][3])
                        turn_queue.remove([turn_queue[0][0], turn_queue[0][1], turn_queue[0][2], turn_queue[0][3]])
                        animation_end = False
                if len(turn_queue) == 0:
                    monster_turn_sign = True

            if monster_turn_sign:
                # 몬스터 체력 0 이하일시 사망처리
                if monster_turn_step == 0:
                    if GPD.monsters[0].HP <= 0 and GPD.monsters[0].act_type != 5:
                        do_monster_animation(2, 0)
                        if animation_end:
                            GPD.monsters[0].act_type = 2
                            animation_end = False
                            monster_turn_step = 1
                    elif GPD.monsters[0].HP > 0 or GPD.monsters[0].act_type == 5:
                        animation_end = False
                        monster_turn_step = 1

                # 몬스터가 모두 죽었으면 전투종료
                elif monster_turn_step == 1:
                    if GPD.monsters[0].HP < 0:
                        game_framework.push_state(battle_win)
                        Battle_is_End = True
                    else:
                        monster_turn_step = 2
                # 몬스터의 공격
                elif monster_turn_step == 2:
                    if GPD.monsters[0].act_type != 5:
                        if monster_NO_deadshot == False:
                            GPD.monsters[0].setting_target()
                            monster_NO_deadshot = True

                        if GPD.monsters[0].act_type is 0 or GPD.monsters[0].act_type is 1:
                            do_monster_animation(1, 0)
                        elif GPD.monsters[0].act_type is 2 or GPD.monsters[0].act_type is 3:
                            do_monster_animation(3, 0)

                        if animation_end:
                            if GPD.monsters[0].act_type is 0:
                                GPD.monsters[0].attack_player()

                            elif GPD.monsters[0].act_type is 2:
                                if GPD.monsters[0].next_skill is 1 or GPD.monsters[0].next_skill is 3:
                                    GPD.monsters[0].FIRE()
                                elif GPD.monsters[0].next_skill is 2 or GPD.monsters[0].next_skill is 4:
                                    GPD.monsters[0].ICE()
                                elif GPD.monsters[0].next_skill is 5 or GPD.monsters[0].next_skill is 6:
                                    GPD.monsters[0].EYES()
                                else:
                                    GPD.monsters[0].COMMON_SKILL()

                            animation_end = False
                            monster_NO_deadshot = False

                            # 플레이어 모두 사망시 게임종료
                            if GPD.players[0].act_type == 7 and \
                                    GPD.players[1].act_type == 7 and \
                                    GPD.players[2].act_type == 7 and \
                                    GPD.players[3].act_type == 7:
                                game_framework.change_state(gameover)

                            monster_turn_step = 3
                    else:
                        monster_turn_step = 3

                # 앞의 플레이어가 죽었을 경우 턴 넘김
                elif monster_turn_step == 3:
                    # 보스 다음 행동 정하기
                    if GPD.monsters[0].phase is 0:
                        dice = random.randint(0, 99)
                        # 평타
                        if number_is_in(0, dice, 24):
                            GPD.monsters[0].act_type = 0
                            # 스키일
                        elif number_is_in(25, dice, 49):
                            GPD.monsters[0].act_type = 2
                            GPD.monsters[0].next_skill = 0
                            # 불 얼음
                        elif number_is_in(50, dice, 74):
                            GPD.monsters[0].act_type = 2
                            GPD.monsters[0].next_skill = 1
                            GPD.monsters[0].FireorIce = 2
                        elif number_is_in(75, dice, 99):
                            GPD.monsters[0].act_type = 2
                            GPD.monsters[0].next_skill = 2
                            GPD.monsters[0].FireorIce = -2
                    elif GPD.monsters[0].phase is 1:
                        dice = random.randint(0, 99)
                        #평타
                        if number_is_in(0, dice, 23):
                            GPD.monsters[0].act_type = 0
                            # 불 얼음
                        elif number_is_in(24, dice, 35):
                            GPD.monsters[0].act_type = 2
                            GPD.monsters[0].next_skill = 1
                            GPD.monsters[0].FireorIce = 2
                        elif number_is_in(36, dice, 47):
                            GPD.monsters[0].act_type = 2
                            GPD.monsters[0].next_skill = 2
                            GPD.monsters[0].FireorIce = -2
                        elif number_is_in(48, dice, 59):
                            GPD.monsters[0].act_type = 2
                            GPD.monsters[0].next_skill = 3
                            GPD.monsters[0].FireorIce = -2
                        elif number_is_in(60, dice, 71):
                            GPD.monsters[0].act_type = 2
                            GPD.monsters[0].next_skill = 4
                            GPD.monsters[0].FireorIce = 2
                            # 눈
                        elif number_is_in(72, dice, 83):
                            GPD.monsters[0].act_type = 2
                            GPD.monsters[0].next_skill = 5
                        elif number_is_in(84, dice, 96):
                            GPD.monsters[0].act_type = 2
                            GPD.monsters[0].next_skill = 6
                            # 거의 전멸기?
                        elif number_is_in(97, dice, 99):
                            GPD.monsters[0].act_type = 2
                            GPD.monsters[0].next_skill = 0

                    player_turn_index = 0
                    for i in range(0, 4):
                        if GPD.players[i].act_type == 7:
                            player_turn_index += 1
                        else:
                            monster_turn_step = 0
                            monster_turn_sign = False
                            turn_end_sign = False
                            break

                # 플레이어가 전부 죽으면 밖으로 나감
                    if player_turn_index == 4:
                        game_framework.change_state(gameover)
                    if GPD.monsters[0].phase is 0 and GPD.monsters[0].HP <= 25000:
                        Phase_Change = True

            Prevtime = current_time


def draw():
    clear_canvas()

    global backgound, turn_image, players, monsters
    global sel_menu_mode, sel_menu_type, player_turn_index

    # 배경 출력
    background_final.clip_draw(0, 0, 1000, 740, 400, 400, 800, 500)
    background.opacify(clamp(0, (GPD.monsters[0].HP - 25000) / 25000, 1.0))
    background.clip_draw(0, 0, 1000, 740, 400, 400, 800, 500)

    # 대상 선택 창
    GPD.Menu.image.clip_draw(0, 0, 240, 160, 75, 75, 150, 150)
    # 스킬 선택 창
    GPD.Menu.image.clip_draw(0, 0, 240, 160, 225, 75, 150, 150)
    # 스킬 선택시 직업에 맞는 스킬 출력
    if sel_menu_mode == 2:
        GPD.Menu.image.clip_draw(242, 84, 17, 16, 180, 120 - menu_index[1] * 30)  # 손가락
        for i in range(0, 4):
            # 마나가 부족하면 회색 그 외엔 흰색
            if GPD.players[player_turn_index].MP < GPD.players[player_turn_index].skill[i].COST:
                GPD.Ingame_font.font.draw(200, 120 - i * 30, GPD.players[player_turn_index].skill[i].name,
                                          [105, 105, 105])
            else:
                GPD.Ingame_font.font.draw(200, 120 - i * 30, GPD.players[player_turn_index].skill[i].name,
                                          [255, 255, 255])
        # 스킬 2차메뉴일때 적 선택
        if sel_menu_type == 2:
            GPD.Menu.image.clip_draw(242, 84, 17, 16, 20, 115 - menu_index[2] * 40)  # 손가락
            for i in range(0, 3):
                # 죽었으면 회색 그 외엔 흰색
                if GPD.monsters[i].act_type == 2:
                    GPD.Ingame_font.font.draw(50, 115 - i * 40, GPD.monsters[i].name, [105, 105, 105])
                else:
                    GPD.Ingame_font.font.draw(50, 115 - i * 40, GPD.monsters[i].name, [255, 255, 255])
        # 아이템 2차메뉴일때 대상선택
        elif sel_menu_type == 3:
            GPD.Menu.image.clip_draw(242, 84, 17, 16, 20, 120 - menu_index[3] * 30)  # 손가락
            for i in range(0, 4):
                # 죽었으면 회색 그 외엔 흰색
                if GPD.players[i].act_type == 7:
                    GPD.Ingame_font.font.draw(50, 120 - i * 30, GPD.players[i].name, [105, 105, 105])
                else:
                    GPD.Ingame_font.font.draw(50, 120 - i * 30, GPD.players[i].name, [255, 255, 255])

    # 아이템 선택시 아이템 목록 출력
    elif sel_menu_mode == 3:
        GPD.Menu.image.clip_draw(242, 84, 17, 16, 170, 120 - menu_index[1] * 30)  # 손가락
        for i in range(0, 4):
            # 없으면 회색 그 외엔 흰색
            if GPD.items[i].NUM == 0:
                GPD.Ingame_font.font.draw(180, 120 - i * 30, GPD.items[i].name + ' ' + str(GPD.items[i].NUM) + '개',
                                          [105, 105, 105])
            else:
                GPD.Ingame_font.font.draw(180, 120 - i * 30, GPD.items[i].name + ' ' + str(GPD.items[i].NUM) + '개',
                                          [255, 255, 255])
        # 아이템 2차메뉴일때 대상선택
        if sel_menu_type == 2:
            GPD.Menu.image.clip_draw(242, 84, 17, 16, 20, 120 - menu_index[2] * 30)  # 손가락
            for i in range(0, 4):
                # 죽었으면 회색 그 외엔 흰색
                if GPD.players[i].act_type == 7:
                    GPD.Ingame_font.font.draw(50, 120 - i * 30, GPD.players[i].name, [105, 105, 105])
                else:
                    GPD.Ingame_font.font.draw(50, 120 - i * 30, GPD.players[i].name, [255, 255, 255])

    # 액션 선택 창
    GPD.Menu.image.clip_draw(0, 0, 240, 160, 400, 75, int(800 / 4), 150)
    GPD.Menu.image.clip_draw(242, 84, 17, 16, 340, 115 - menu_index[0] * 40)  # 손가락
    GPD.Ingame_font.font.draw(360, 115 - 0 * 40, '공격', [255, 255, 255])
    GPD.Ingame_font.font.draw(360, 115 - 1 * 40, '스킬', [255, 255, 255])
    GPD.Ingame_font.font.draw(360, 115 - 2 * 40, '아이템', [255, 255, 255])

    # 아군 상태 출력
    GPD.Menu.image.clip_draw(0, 0, 240, 160, 650, 75, int(800 / 4 * 3 / 2), 150)
    for i in range(0, 4):
        # 죽었으면 회색 그 외엔 흰색
        if GPD.players[i].act_type == 7:
            GPD.Ingame_font.font.draw(550, 120 - i * 30, GPD.players[i].status_string, [105, 105, 105])
        else:
            GPD.Ingame_font.font.draw(550, 120 - i * 30, GPD.players[i].status_string, [255, 255, 255])

    if monster_turn_sign == False and turn_end_sign == False:
        turn_image.clip_draw(0, 0, 72, 72, 600, 420 - 75 * player_turn_index)
    # 플레이어 출력
    for i in range(0, 4):
        GPD.players[i].draw()
    # 몬스터 출력
    GPD.monsters[0].draw()

    # 이펙트 출력
    if len(turn_queue):
        if turn_queue[0][0] == 1:
            GPD.effects.draw(turn_queue[0][1], turn_queue[0][2])
        elif turn_queue[0][0] == 2:
            GPD.effects.draw(turn_queue[0][1], -1)
        else:
            GPD.effects.draw(turn_queue[0][1], turn_queue[0][3])

    if monster_turn_sign:
        GPD.effects.draw(0, GPD.monsters[0].attack_target)

    BattlelogBack.clip_draw(0, 0, 1, 1, 400, 150 + 15 * len(GPD.Battlelog), 250, 30 * len(GPD.Battlelog))
    for i in range(0, len(GPD.Battlelog)):
        GPD.Ingame_font.font.draw(275, (130 + len(GPD.Battlelog) * 30) - i * 30, GPD.Battlelog[i],
                                  [255, 255, 255])

    update_canvas()


def pause(): pass


def resume(): pass


def handle_events():
    global running
    global sel_menu_type, sel_menu_mode, menu_index
    global turn_queue, player_turn_index, turn_end_sign
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            pass
        # a 선택 s 뒤로가기
        elif event.type == SDL_KEYDOWN and turn_end_sign is False:
            GPD.Menu.sound.play()
            #if event.key == SDLK_ESCAPE:
                # game_framework.change_state(map)
                #game_framework.pop_state()

            # 기본 메뉴 일때
            if sel_menu_mode == 0:
                # 방향키로 위아래
                if event.key == SDLK_UP:
                    if menu_index[sel_menu_type] > 0:
                        menu_index[sel_menu_type] -= 1
                elif event.key == SDLK_DOWN:
                    if menu_index[sel_menu_type] < 2:
                        menu_index[sel_menu_type] += 1
                # a키로 선택
                # 2차메뉴로 들어감
                elif event.key == SDLK_a:
                    sel_menu_mode = menu_index[sel_menu_type] + 1
                    sel_menu_type = 1
                    # 공격 메뉴 일때
                    if sel_menu_mode == 1:
                        turn_queue.append([1, player_turn_index, 0])
                        GPD.players[player_turn_index].act_type = 1
                        sel_menu_type -= 1
                        sel_menu_mode = 0

                        initialize_menu_index(0, 2)

                        if player_turn_index == 3:
                            turn_end_sign = True
                            player_turn_index = 0
                        else:
                            player_turn_index += 1
                            # 앞에놈 죽었으면 턴 넘김
                            while GPD.players[player_turn_index].act_type == 7:
                                player_turn_index += 1
                                # 마지막놈이 죽었으면 그대로 턴 종료
                                if player_turn_index == 4:
                                    turn_end_sign = True
                                    break

            # 스킬 메뉴 일때
            elif sel_menu_mode == 2:
                # 방향키로 위아래
                if event.key == SDLK_UP:
                    if menu_index[sel_menu_type] > 0:
                        menu_index[sel_menu_type] -= 1
                elif event.key == SDLK_DOWN:
                    if menu_index[sel_menu_type] < 3:
                        menu_index[sel_menu_type] += 1
                elif event.key == SDLK_a:
                    # 스킬 선택
                    if sel_menu_type == 1:
                        if GPD.players[player_turn_index].MP >= GPD.players[player_turn_index].skill[
                            menu_index[sel_menu_type]].COST:
                            ID = GPD.players[player_turn_index].skill[menu_index[sel_menu_type]].ID
                            # 대상 선택 미필요
                            if ID == 2 or ID == 3 or ID == 7 or ID == 8 or ID == 10 or ID == 11 \
                                    or ID == 14 or ID == 16:
                                turn_queue.append([2, player_turn_index, menu_index[1]])

                                GPD.players[player_turn_index].act_type = 1
                                sel_menu_type -= 1
                                sel_menu_mode = 0

                                initialize_menu_index(0, 2)

                                if player_turn_index == 3:
                                    turn_end_sign = True
                                else:
                                    player_turn_index += 1
                                    # 앞에놈 죽었으면 턴 넘김
                                    while GPD.players[player_turn_index].act_type == 7:
                                        player_turn_index += 1
                                        # 마지막놈이 죽었으면 그대로 턴 종료
                                        if player_turn_index == 4:
                                            turn_end_sign = True
                                            break
                            # 대상 선택 : 적군
                            elif ID == 1 or ID == 4 or ID == 5 or ID == 9 or ID == 13 or ID == 15:
                                    turn_queue.append([3, player_turn_index, menu_index[1], 0])
                                    GPD.players[player_turn_index].act_type = 1
                                    sel_menu_type -= 1
                                    sel_menu_mode = 0

                                    initialize_menu_index(0, 2)

                                    if player_turn_index == 3:
                                        turn_end_sign = True
                                    else:
                                        player_turn_index += 1
                                        # 앞에놈 죽었으면 턴 넘김
                                        while GPD.players[player_turn_index].act_type == 7:
                                            player_turn_index += 1
                                            # 마지막놈이 죽었으면 그대로 턴 종료
                                            if player_turn_index == 4:
                                                turn_end_sign = True
                                                break
                            # 대상 선택 : 아군
                            else:
                                sel_menu_type += 2
                    # 대상선택
                    elif sel_menu_type == 3:
                        # 플레이어 죽은건 선택 못함
                        if GPD.players[menu_index[3]].act_type != 7:
                            turn_queue.append([3, player_turn_index, menu_index[1], menu_index[3]])
                            GPD.players[player_turn_index].act_type = 1
                            sel_menu_type -= 3
                            sel_menu_mode = 0

                            initialize_menu_index(0, 3)

                            if player_turn_index == 3:
                                turn_end_sign = True
                            else:
                                player_turn_index += 1
                                # 앞에놈 죽었으면 턴 넘김
                                while GPD.players[player_turn_index].act_type == 7:
                                    player_turn_index += 1
                                    # 마지막놈이 죽었으면 그대로 턴 종료
                                    if player_turn_index == 4:
                                        turn_end_sign = True
                                        break
                # 뒤로가기
                elif event.key == SDLK_s:
                    sel_menu_mode = 0
                    sel_menu_type = 0
                    initialize_menu_index(1, 2)

            # 아이템 메뉴 일때
            elif sel_menu_mode == 3:
                # 방향키로 위아래
                if event.key == SDLK_UP:
                    if menu_index[sel_menu_type] > 0:
                        menu_index[sel_menu_type] -= 1
                elif event.key == SDLK_DOWN:
                    if menu_index[sel_menu_type] < 3:
                        menu_index[sel_menu_type] += 1
                elif event.key == SDLK_a:
                    # 아이템 선택
                    if sel_menu_type == 1:
                        if GPD.items[menu_index[sel_menu_type]].NUM != 0:
                            sel_menu_type += 1
                    # 대상 선택
                    elif sel_menu_type == 2:
                        turn_queue.append([4, player_turn_index, menu_index[1], menu_index[2]])
                        GPD.items[menu_index[1]].NUM -= 1
                        sel_menu_type -= 2
                        sel_menu_mode = 0

                        initialize_menu_index(0, 2)

                        if player_turn_index == 3:
                            turn_end_sign = True
                        else:
                            player_turn_index += 1
                            # 앞에놈 죽었으면 턴 넘김
                            while GPD.players[player_turn_index].act_type == 7:
                                player_turn_index += 1
                                # 마지막놈이 죽었으면 그대로 턴 종료
                                if player_turn_index == 4:
                                    turn_end_sign = True
                                    break
                # 뒤로가기
                elif event.key == SDLK_s:
                    if sel_menu_type == 1:
                        sel_menu_mode = 0
                        initialize_menu_index(1, 2)
                    sel_menu_type -= 1
                    initialize_menu_index(2, 2)



def do_player_animation():
    global turn_queue
    global animation_end
    global current_time, Prevtime

    # 평타
    if turn_queue[0][0] == 1:
        # 앞으로 이동
        if GPD.players[turn_queue[0][1]].anistep == 0:
            GPD.players[turn_queue[0][1]].attack_animation -= 150 * (current_time - Prevtime)
            if GPD.players[turn_queue[0][1]].attack_animation <= -100:
                GPD.players[turn_queue[0][1]].act_type = 2
                GPD.players[turn_queue[0][1]].frame = 0
                GPD.players[turn_queue[0][1]].anistep = 1
        # 공격
        elif GPD.players[turn_queue[0][1]].anistep == 1:
            if GPD.players[turn_queue[0][1]].frame >= 2:
                GPD.effects.frame = 0
                GPD.effects.id = 0
                GPD.players[turn_queue[0][1]].anistep = 2
                GPD.effects.playFX()
        # 이펙트
        elif GPD.players[turn_queue[0][1]].anistep == 2:
            if GPD.effects.frame < 2:
                GPD.effects.frame += 10 * game_framework.frame_time
            elif GPD.effects.frame >= 2:
                GPD.effects.frame = 0
                GPD.effects.id = -1
                GPD.players[turn_queue[0][1]].act_type = 0
                GPD.players[turn_queue[0][1]].anistep = 3
        # 뒤로 이동
        elif GPD.players[turn_queue[0][1]].anistep == 3:
            if GPD.players[turn_queue[0][1]].attack_animation < 0:
                GPD.players[turn_queue[0][1]].attack_animation += 150 * (current_time - Prevtime)
            else:
                set_player_acttype(turn_queue[0][1])
                GPD.players[turn_queue[0][1]].anistep = 0
                animation_end = True

    # 스킬 사용
    elif turn_queue[0][0] == 2 or turn_queue[0][0] == 3:
        # 앞으로 이동
        if GPD.players[turn_queue[0][1]].anistep == 0:
            GPD.players[turn_queue[0][1]].attack_animation -= 150 * (current_time - Prevtime)
            if GPD.players[turn_queue[0][1]].attack_animation <= -100:
                GPD.effects.frame = 0
                GPD.effects.id = 10 + GPD.players[turn_queue[0][1]].skill[turn_queue[0][2]].ID
                GPD.players[turn_queue[0][1]].anistep = 1
                GPD.effects.playFX()
        # 이펙트
        elif GPD.players[turn_queue[0][1]].anistep == 1:
            if GPD.effects.frame < GPD.skill_MAXframe[GPD.effects.id]:
                GPD.effects.frame += 30 * game_framework.frame_time
            elif GPD.effects.frame >= GPD.skill_MAXframe[GPD.effects.id]:
                GPD.effects.frame = 0
                GPD.effects.id = -1
                GPD.players[turn_queue[0][1]].act_type = 0
                GPD.players[turn_queue[0][1]].anistep = 2
        # 뒤로 이동
        elif GPD.players[turn_queue[0][1]].anistep == 2:
            if GPD.players[turn_queue[0][1]].attack_animation < 0:
                GPD.players[turn_queue[0][1]].attack_animation += 150 * (current_time - Prevtime)
            else:
                set_player_acttype(turn_queue[0][1])
                GPD.players[turn_queue[0][1]].anistep = 0
                animation_end = True

    # 아이템 사용
    elif turn_queue[0][0] == 4:
        # 기모음
        if GPD.players[turn_queue[0][1]].anistep == 0:
            GPD.players[turn_queue[0][1]].act_type = 3
            GPD.players[turn_queue[0][1]].frame = 0
            GPD.players[turn_queue[0][1]].anistep = 1

        elif GPD.players[turn_queue[0][1]].anistep == 1:
            if GPD.players[turn_queue[0][1]].frame <= 1:
                GPD.players[turn_queue[0][1]].frame += 120 * (current_time - Prevtime)
            else:
                GPD.players[turn_queue[0][1]].anistep = 2

        # 이펙트
        if GPD.players[turn_queue[0][1]].anistep == 2:
            GPD.effects.frame = 0
            GPD.players[turn_queue[0][1]].anistep = 3
            GPD.effects.playFX()

        if GPD.players[turn_queue[0][1]].anistep == 3:
            # 부활템 일떄
            if turn_queue[0][2] == 3:
                GPD.effects.id = 2
                if GPD.effects.frame < 29:
                    GPD.effects.frame += 5 * (current_time - Prevtime)
                elif GPD.effects.frame >= 29:
                    GPD.players[turn_queue[0][1]].anistep = 4
            # 그 외의 경우
            else:
                GPD.effects.id = 1
                if GPD.effects.frame < 20:
                    GPD.effects.frame += 15 * (current_time - Prevtime)
                if GPD.effects.frame >= 20:
                    GPD.players[turn_queue[0][1]].anistep = 4

        if GPD.players[turn_queue[0][1]].anistep == 4:
            GPD.effects.frame = 0
            GPD.effects.id = -1
            GPD.players[turn_queue[0][1]].anistep = 0
            set_player_acttype(turn_queue[0][1])
            animation_end = True


def do_monster_animation(id, index):
    global turn_queue
    global animation_end
    global timer

    # 평타
    if id == 1:
        # 공격
        if GPD.monsters[index].anistep == 0:
            GPD.monsters[index].act_type = 1
            GPD.monsters[index].frame = 0
            GPD.monsters[index].anistep = 1
            GPD.monsters[index].sound.play()

        if GPD.monsters[index].anistep == 1:
            if GPD.monsters[index].frame >= 30:
                GPD.effects.id = 100
                GPD.monsters[index].anistep = 2
                GPD.players[GPD.monsters[index].attack_target].act_type = 6
                GPD.effects.playFX()

        if GPD.monsters[index].anistep == 2:
            if GPD.effects.frame < GPD.skill_MAXframe[GPD.effects.id]:
                GPD.effects.frame += 10 * game_framework.frame_time
            elif GPD.effects.frame >= GPD.skill_MAXframe[GPD.effects.id]:
                GPD.effects.frame = 0
                GPD.effects.id = -1
                GPD.monsters[index].anistep = 3

        if GPD.monsters[index].anistep == 3:
            set_player_acttype(GPD.monsters[index].attack_target)
            set_monster_acttype(index)
            GPD.monsters[index].anistep = 0
            animation_end = True
    # 죽을때
    elif id == 2:
        if GPD.monsters[index].anistep == 0:
            if GPD.monsters[index].die_animation < 72:
                GPD.monsters[index].die_animation += 200 * (current_time - Prevtime)
            elif GPD.monsters[index].die_animation >= 72:
                GPD.monsters[index].sound.play()
                animation_end = True
    # 스킬
    elif id == 3:
        if GPD.monsters[index].anistep == 0:
            GPD.monsters[index].sound.play()
            GPD.monsters[index].act_type = 3
            GPD.monsters[index].frame = 0
            GPD.monsters[index].anistep = 1

        if GPD.monsters[index].anistep == 1:
            if GPD.monsters[index].frame >= 12:
                GPD.effects.id = 200 + GPD.monsters[index].next_skill
                GPD.effects.playFX()
                GPD.monsters[index].anistep = 2
                for i in range(0,4):
                    if GPD.players[i].HP > 0:
                        GPD.players[i].act_type = 6

        if GPD.monsters[index].anistep == 2:
            if GPD.effects.frame < GPD.skill_MAXframe[GPD.effects.id]:
                GPD.effects.frame += 30 * game_framework.frame_time
            elif GPD.effects.frame >= GPD.skill_MAXframe[GPD.effects.id]:
                GPD.effects.frame = 0
                GPD.effects.id = -1
                GPD.monsters[index].anistep = 3

        if GPD.monsters[index].anistep == 3:
            for i in range(0, 4):
                set_player_acttype(i)
            set_monster_acttype(index)
            GPD.monsters[index].anistep = 0
            animation_end = True


def set_player_acttype(index):
    if GPD.players[index].HP / GPD.players[index].MAX_HP <= 0.2:
        GPD.players[index].act_type = 5
    else:
        GPD.players[index].act_type = 0
    if GPD.players[index].HP <= 0:
        GPD.players[index].act_type = 7


def set_monster_acttype(index):
    if GPD.monsters[index].act_type is 1:
        GPD.monsters[index].act_type = 0
    elif GPD.monsters[index].act_type is 3:
        GPD.monsters[index].act_type = 2


# 메뉴인덱스 초기화
def initialize_menu_index(start, end):
    global menu_index
    for i in range(start, end + 1):
        menu_index[i] = 0


# @ 하고 # 사이 값이면 TRUE 리턴
def number_is_in(start, number, end):
    if number >= start and number <= end:
        return True
    else:
        return False
