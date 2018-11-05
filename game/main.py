from pico2d import*
import game_framework

import title

import Game_Playing_Data
import p_warrior
import i_HPpotion
import i_MPpotion
import i_Curepotion
import i_PhoenixDown

open_canvas(800,600)



for i in range(0,4):
    Game_Playing_Data.players[i]=p_warrior.Warrior(i)


Game_Playing_Data.items[0]=i_HPpotion.HPpotion()
Game_Playing_Data.items[1]=i_MPpotion.MPpotion()
Game_Playing_Data.items[2]=i_Curepotion.Curepotion()
Game_Playing_Data.items[3]=i_PhoenixDown.PhoenixDown()

game_framework.run(title)

close_canvas()