from monster_spawner import*
from pico2d import*
import random
from overworld_load import FixedTileBackground as Background
import game_framework
import battle, pause_menu
import dungeon
import town
import GamePlayingData as GPD
import BaseEffect
import Bounding_box



WIDTH=800
HEIGHT=600

background = None

Cant_Move_Tile = []
Entrance_Tile = []

def enter():
    global current_time, Prevtime
    global background, Cant_Move_Tile, Entrance_Tile

    current_time = 0
    Prevtime = 0

    GPD.Upload_data()

    background = Background()

    GPD.Player.set_background(background)
    background.set_center_object(GPD.Player)
    background.update()

    Cant_Move_Tile = [Bounding_box.BaseZone(background.tile_map.layers[1]['objects'][i],1600)
                     for i in range(len(background.tile_map.layers[1]['objects']))]
    Entrance_Tile = [Bounding_box.BaseZone(background.tile_map.layers[2]['objects'][i],1600)
                     for i in range(len(background.tile_map.layers[2]['objects']))]

    GPD.bgm = load_music("sound\\bgm\\Overworld.mp3")
    GPD.bgm.repeat_play()

    # 캐릭터 초기 시작위치
    if GPD.now_map is -1:
        GPD.Player.x = GPD.x
        GPD.Player.y = GPD.y
        pass

    elif GPD.now_map is 0:
        GPD.Player.x = GPD.x
        GPD.Player.y = GPD.y
        GPD.Player.state = 0

    elif GPD.now_map is 1:
        GPD.Player.x = 461
        GPD.Player.y = 353

    elif GPD.now_map is 2:
        GPD.Player.x = 506
        GPD.Player.y = 1109

    GPD.Player.bg.w = 1600
    GPD.Player.bg.h = 1600
    GPD.now_map = 0


def exit():
    if GPD.bgm is not None:
        GPD.bgm.stop()
        del (GPD.bgm)
        GPD.bgm = None
    pass


def update():
    global Cant_Move_Tile, Entrance_Tile
    global current_time, Prevtime

    current_time = get_time()

    if current_time - Prevtime > 1 / 60:
        background.update()
        backup_x, backup_y = GPD.Player.x, GPD.Player.y
        GPD.Player.update()

        for Zone in Cant_Move_Tile:
            if collide(GPD.Player, Zone):
                GPD.Player.x = backup_x
                GPD.Player.y = backup_y
                break

        if collide(GPD.Player, Entrance_Tile[0]):
            game_framework.change_state(town)
        elif collide(GPD.Player, Entrance_Tile[1]):
            game_framework.change_state(dungeon)

        if GPD.Player.battle_counter <= 0:
            GPD.Player.battle_counter = 30 + random.randint(0,10)
            start_battle()

        #SAVE_Manager.Save_game()

        Prevtime = current_time


def draw():
    global background
    clear_canvas()
    background.draw()
    GPD.Player.draw()
    GPD.Player.draw_bb()
    for Zone in Cant_Move_Tile:
        Zone.draw_bb(background)
    GPD.Ingame_font.font.draw(75, 115, str(GPD.Player.battle_counter), [255, 255, 255])
    update_canvas()


def pause():
    pass


def resume():
    if GPD.bgm is None:
        GPD.bgm = load_music("sound\\bgm\\Overworld.mp3")
        GPD.bgm.repeat_play()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(pause_menu)
            # 강제 배틀 돌입
        elif event.type == SDL_KEYDOWN and event.key == SDLK_0:
            start_battle()
        else:
            GPD.Player.handle_events(event)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False
    return True


def start_battle():
    if GPD.bgm is not None:
        GPD.bgm.stop()
        del (GPD.bgm)
        GPD.bgm = None
    for i in range(0, 4):
        GPD.Player.move_dir[i] = 0
    Generate_monster()
    if GPD.effects == None:
        GPD.effects = BaseEffect.Effect()
    game_framework.push_state(battle)