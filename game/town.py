from pico2d import*
from town_load import FixedTileBackground as Background
from overworld_charactrer import Character as Character
import game_framework
import Game_Playing_Data as GPD
import Bounding_box
import overworld
import shop_potion, shop_skill, shop_motel


WIDTH=800
HEIGHT=600

background = None
Cant_Move_Tile = []
Entrance_Tile = []

def enter():
    global character
    global current_time, Prevtime
    global background, Cant_Move_Tile, Entrance_Tile
    #open_canvas(WIDTH,HEIGHT)

    current_time = 0
    Prevtime = 0

    character = Character()
    background = Background()

    character.set_background(background)
    background.set_center_object(character)
    background.update()

    Cant_Move_Tile = [Bounding_box.BaseZone(background.tile_map.layers[1]['objects'][i],960)
                     for i in range(len(background.tile_map.layers[1]['objects']))]
    Entrance_Tile = [Bounding_box.BaseZone(background.tile_map.layers[2]['objects'][i],960)
                     for i in range(len(background.tile_map.layers[2]['objects']))]

    # 캐릭터 시작위치
    character.x = GPD.x
    character.y = GPD.y
    character.bg.w = GPD.bg_x
    character.bg.h = GPD.bg_y

    if GPD.now_map == 0:
        character.x = 461
        character.y = 353
        character.bg.w = 960
        character.bg.h = 960
        character.state = 0

    GPD.Upload_data()
    GPD.now_map = 2


def exit():
    pass


def update():
    global character, Cant_Move_Tile, Entrance_Tile
    global current_time, Prevtime

    current_time = get_time()

    if current_time - Prevtime > 1 / 60:
        collide_zone = []
        background.update()
        backup_x, backup_y = character.x, character.y
        character.update()

        for Zone in Cant_Move_Tile:
            if collide(character, Zone):
                character.x = backup_x
                character.y = backup_y
                break

        # 스킬상점
        if collide(character, Entrance_Tile[0]):
            game_framework.push_state(shop_skill)
            character.y -= 50
            character.move_dir = [0, 0, 0, 0]
            character.state = 0
        # 잡화상점
        elif collide(character, Entrance_Tile[1]):
            game_framework.push_state(shop_potion)
            character.y -= 50
            character.move_dir = [0, 0, 0, 0]
            character.state = 0
        # 여관
        elif collide(character, Entrance_Tile[2]):
            game_framework.push_state(shop_motel)
            character.y -= 50
            character.move_dir = [0, 0, 0, 0]
            character.state = 0
            pass
        # 출구
        elif collide(character, Entrance_Tile[3]):
            game_framework.change_state(overworld)

        if character.battle_counter <= 0:
            character.battle_counter = 40

        Prevtime = current_time


def draw():
    global background
    clear_canvas()
    background.draw()
    character.draw()
    character.draw_bb()
    for Zone in Cant_Move_Tile:
        Zone.draw_bb(background)
    GPD.Ingame_font.font.draw(75, 115, str(character.battle_counter), [255, 255, 255])
    update_canvas()


def pause(): pass


def resume(): pass


def handle_events():
    global character

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
             character.handle_events(event)


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
