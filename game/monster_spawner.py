from m_Wolf import*
from m_Chocobo import*
from m_Bat import*
from m_BlueBomb import*
from m_Dragon import*
from m_Flower import*
from m_Mutalisk import*
from m_RedBomb import*
from m_ShieldMan import*
from m_Slime import*
from m_Snake import*
import GamePlayingData as GPD
import random


def Generate_monster():
    average_level = (GPD.players[0].LEVEL + GPD.players[1].LEVEL + GPD.players[2].LEVEL + GPD.players[3].LEVEL) / 4
    monster_num = 0

    while monster_num < 3:
        dice = random.randint(0, 10)

        if average_level < 5:
            if dice is 0:
                GPD.monsters[monster_num] = Wolf(monster_num)
            elif dice is 1:
                GPD.monsters[monster_num] = Chocobo(monster_num)
            elif dice is 2:
                GPD.monsters[monster_num] = Bat(monster_num)
            elif dice is 3:
                GPD.monsters[monster_num] = BlueBomb(monster_num)
            elif dice is 4:
                GPD.monsters[monster_num] = Dragon(monster_num)
            elif dice is 5:
                GPD.monsters[monster_num] = Flower(monster_num)
            elif dice is 6:
                GPD.monsters[monster_num] = Mutalisk(monster_num)
            elif dice is 7:
                GPD.monsters[monster_num] = RedBomb(monster_num)
            elif dice is 8:
                GPD.monsters[monster_num] = ShieldMan(monster_num)
            elif dice is 9:
                GPD.monsters[monster_num] = Slime(monster_num)
            elif dice is 10:
                GPD.monsters[monster_num] = Snake(monster_num)

        monster_num += 1

