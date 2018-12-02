from pico2d import*
from town_load import FixedTileBackground as Background
import game_framework
import GamePlayingData as GPD
import Bounding_box
import overworld, pause_menu
import shop_potion, shop_skill, shop_motel


WIDTH=800
HEIGHT=600

background = None
Cant_Move_Tile = []
Entrance_Tile = []

def enter():
    global current_time, Prevtime
    global background, Cant_Move_Tile, Entrance_Tile
    #open_canvas(WIDTH,HEIGHT)

    current_time = 0
    Prevtime = 0

    GPD.Upload_data()

    background = Background()

    GPD.Player.set_background(background)
    background.set_center_object(GPD.Player)
    background.update()

    Cant_Move_Tile = [Bounding_box.BaseZone(background.tile_map.layers[1]['objects'][i],960)
                     for i in range(len(background.tile_map.layers[1]['objects']))]
    Entrance_Tile = [Bounding_box.BaseZone(background.tile_map.layers[2]['objects'][i],960)
                     for i in range(len(background.tile_map.layers[2]['objects']))]

    GPD.bgm.town.repeat_play()

    # 캐릭터 초기  시작위치
    GPD.Player.x = GPD.x
    GPD.Player.y = GPD.y
    GPD.Player.bg.w = 960
    GPD.Player.bg.h = 960
    GPD.Player.state = 1

    if GPD.now_map == 0:
        GPD.Player.x = 398
        GPD.Player.y = 100

    GPD.now_map = 2


def exit():
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

        # 스킬상점
        if collide(GPD.Player, Entrance_Tile[0]):
            GPD.isMenunow = True
            game_framework.push_state(shop_skill)
            GPD.Player.y -= 50
            GPD.Player.move_dir = [0, 0, 0, 0]
            GPD.Player.state = 0
        # 잡화상점
        elif collide(GPD.Player, Entrance_Tile[1]):
            GPD.isMenunow = True
            game_framework.push_state(shop_potion)
            GPD.Player.y -= 50
            GPD.Player.move_dir = [0, 0, 0, 0]
            GPD.Player.state = 0
        # 여관
        elif collide(GPD.Player, Entrance_Tile[2]):
            GPD.isMenunow = True
            game_framework.push_state(shop_motel)
            GPD.Player.y -= 50
            GPD.Player.move_dir = [0, 0, 0, 0]
            GPD.Player.state = 0
            pass
        # 출구
        elif collide(GPD.Player, Entrance_Tile[3]):
            game_framework.change_state(overworld)

        if GPD.Player.battle_counter <= 0:
            GPD.Player.battle_counter = 40

        Prevtime = current_time


def draw():
    global background
    clear_canvas()
    background.draw()
    GPD.Player.draw()
    GPD.Player.draw_bb()
    #for Zone in Cant_Move_Tile:
        #Zone.draw_bb(background)
    #GPD.Ingame_font.font.draw(75, 115, str(GPD.Player.battle_counter), [255, 255, 255])
    update_canvas()


def pause(): pass


def resume():
    if GPD.isMenunow == False:
        GPD.bgm.town.repeat_play()
    GPD.isMenunow=False


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            GPD.isMenunow = True
            game_framework.push_state(pause_menu)
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
