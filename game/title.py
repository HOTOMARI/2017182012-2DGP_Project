from pico2d import*
import GamePlayingData as GPD
import subprocess
import game_framework
import overworld, dungeon, town
import p_Warrior, p_WhiteMage, p_BlackMage, p_Thief
import i_HPpotion, i_MPpotion, i_Curepotion, i_PhoenixDown

import SAVEManager

background = None
logo = None
time = 0

def enter():
    global background, logo
    global sel_index
    GPD.Upload_data()
    background = load_image("image\\title\\background.png")
    logo = load_image("image\\title\\logo.png")
    #GPD.bgm = load_music("sound\\bgm\\Title.mp3")
    #GPD.bgm.set_volume(64)
    #GPD.bgm.repeat_play()
    sel_index = 0

def exit():
    #GPD.bgm.stop()
    #del(GPD.bgm)
    #GPD.bgm = None
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

def pause():
    pass

def resume():
    pass

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
                    New_Game()
                    GPD.now_map = 0
                    game_framework.change_state(overworld)
                elif sel_index is 1:
                    New_Game()
                    SAVEManager.Load_game()
                    if GPD.now_map is 0:
                        GPD.now_map = -1
                        game_framework.change_state(overworld)
                    elif GPD.now_map is 1:
                        GPD.now_map = -1
                        game_framework.change_state(dungeon)
                    elif GPD.now_map is 2:
                        GPD.now_map = -1
                        game_framework.change_state(town)
                elif sel_index is 2:
                    subprocess.call('howtoplay.bat')
                    pass
                elif sel_index is 3:
                    game_framework.quit()
            elif event.key == SDLK_UP:
                GPD.Menu.sound.play()
                if sel_index > 0:
                    sel_index -= 1
            elif event.key == SDLK_DOWN:
                GPD.Menu.sound.play()
                if sel_index < 3:
                    sel_index += 1


def New_Game():
    GPD.money = 400
    GPD.now_map = 0  # 0 초원 1 던전 2 마을
    GPD.x, GPD.y = 506, 1109

    GPD.players[0] = p_Warrior.Warrior(0)
    GPD.players[1] = p_WhiteMage.WhiteMage(1)
    GPD.players[2] = p_Thief.Thief(2)
    GPD.players[3] = p_BlackMage.BlackMage(3)

    GPD.items[0] = i_HPpotion.HPpotion()
    GPD.items[1] = i_MPpotion.MPpotion()
    GPD.items[2] = i_Curepotion.Curepotion()
    GPD.items[3] = i_PhoenixDown.PhoenixDown()
    pass