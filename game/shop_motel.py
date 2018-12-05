from pico2d import *
import game_framework
import GamePlayingData as GPD
import SAVEManager

White_font = [255, 255, 255]
Gray_font = [105, 105, 105]

background = None

def enter():
    global current_time, Prevtime
    global background, shop_mode, system_message
    current_time = 0
    Prevtime = 0
    shop_mode = 0
    system_message = ""

    if background is None:
        background = load_image('image\\black_point.png')


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
    background.clip_draw(0, 0, 1, 1, 400, 300, 800, 600)
    GPD.Menu.image.clip_draw(1, 1, 240, 160, 400, 300, 300, 200)

    # 안내문
    GPD.Ingame_font.font.draw(300, 350, "모든 HP와 MP를 회복하고.", White_font)
    GPD.Ingame_font.font.draw(300, 300, "현재 데이터를 저장합니다.", White_font)
    GPD.Ingame_font.font.draw(300, 250, "필요한 돈: 200", White_font)
    GPD.Ingame_font.font.draw(400, 250, "현재 돈: "+ str(GPD.money), White_font)

    GPD.Ingame_Big_font.font.draw(400-len(system_message)*7, 150, system_message, [255,0,0])

    update_canvas()


def pause(): pass


def resume(): pass


def handle_events():
    global shop_mode, system_message

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
                    if GPD.money < 200:
                        system_message = "돈이 부족합니다!"
                    else:
                        GPD.money -= 200
                        for i in range (0,4):
                            GPD.players[i].HP = GPD.players[i].MAX_HP
                            GPD.players[i].MP = GPD.players[i].MAX_MP
                        system_message = "데이터를 저장합니다."
                        SAVEManager.Save_game()
                        system_message = "데이터 저장이 완료되었습니다."
                        shop_mode = 1
                elif shop_mode == 1:
                    game_framework.pop_state()

            elif event.key == SDLK_s:
                if shop_mode == 0:
                    game_framework.pop_state()
