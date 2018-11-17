from m_Wolf import*
from m_Chocobo import*
import GamePlayingData as GPD
import random

def Generate_monster():
    average_level = (GPD.players[0].LEVEL + GPD.players[1].LEVEL + GPD.players[2].LEVEL + GPD.players[3].LEVEL) / 4
    monster_num = 0

    while monster_num < 3:
        dice = random.randint(0, 10)
        
        if average_level < 5:
            if dice < 6:
                GPD.monsters[monster_num] = Wolf(monster_num)
            else:
                GPD.monsters[monster_num] = Chocobo(monster_num)

        monster_num += 1

