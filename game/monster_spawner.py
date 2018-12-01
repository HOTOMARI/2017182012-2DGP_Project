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

    while len(GPD.monsters) < 3:
        dice = random.randint(0, 10)

        if average_level < 5:
            GPD.monsters.append(Wolf(monster_num))
        elif average_level < 15:
            if dice < 3:
                GPD.monsters.append(Wolf(monster_num))
            elif dice < 8:
                GPD.monsters.append(Chocobo(monster_num))
            else:
                GPD.monsters.append(Slime(monster_num))
        elif average_level < 30:
            if dice < 2:
                GPD.monsters.append(Chocobo(monster_num))
            elif dice < 5:
                GPD.monsters.append(BlueBomb(monster_num))
            elif dice < 7:
                GPD.monsters.append(RedBomb(monster_num))
            elif dice < 9:
                GPD.monsters.append(ShieldMan(monster_num))
            else:
                GPD.monsters.append(Slime(monster_num))
        elif average_level < 50:
            if dice < 2:
                GPD.monsters.append(Bat(monster_num))
            elif dice < 4:
                GPD.monsters.append(BlueBomb(monster_num))
            elif dice < 5:
                GPD.monsters.append(Dragon(monster_num))
            elif dice < 7:
                GPD.monsters.append(RedBomb(monster_num))
            elif dice < 8:
                GPD.monsters.append(ShieldMan(monster_num))
            else:
                GPD.monsters.append(Slime(monster_num))
        elif average_level < 70:
            if dice < 2:
                GPD.monsters.append(Bat(monster_num))
            elif dice < 5:
                GPD.monsters.append(Dragon(monster_num))
            elif dice < 8:
                GPD.monsters.append(Mutalisk(monster_num))
            else:
                GPD.monsters.append(Snake(monster_num))
        elif average_level < 90:
            if dice is 0:
                GPD.monsters.append(Wolf(monster_num))
            elif dice is 1:
                GPD.monsters.append(Bat(monster_num))
            elif dice is 2:
                GPD.monsters.append(Dragon(monster_num))
            elif dice < 4:
                GPD.monsters.append(Flower(monster_num))
            elif dice < 7:
                GPD.monsters.append(Mutalisk(monster_num))
            else:
                GPD.monsters.append(Snake(monster_num))
        else:
            if dice is 0:
                GPD.monsters.append(Wolf(monster_num))
            elif dice is 1:
                GPD.monsters.append(Chocobo(monster_num))
            elif dice is 2:
                GPD.monsters.append(Bat(monster_num))
            elif dice is 3:
                GPD.monsters.append(BlueBomb(monster_num))
            elif dice is 4:
                GPD.monsters.append(Dragon(monster_num))
            elif dice is 5:
                GPD.monsters.append(Flower(monster_num))
            elif dice is 6:
                GPD.monsters.append(Mutalisk(monster_num))
            elif dice is 7:
                GPD.monsters.append(RedBomb(monster_num))
            elif dice is 8:
                GPD.monsters.append(ShieldMan(monster_num))
            elif dice is 9:
                GPD.monsters.append(Slime(monster_num))
            elif dice is 10:
                GPD.monsters.append(Snake(monster_num))

        monster_num += 1
