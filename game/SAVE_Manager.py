import Game_Playing_Data as GPD


def Save_game():
    f = open('test.txt', mode='wt')
    # 캐릭터 위치
    f.write(str(GPD.now_map) + '\n' + str(GPD.Player.x) + '\n' + str(GPD.Player.y) + '\n')
    # 아이템 정보
    f.write(str(GPD.money) + '\n')
    for i in range(0,4):
        f.write(str(GPD.items[i].NUM)+'\n')

    # 캐릭터 정보
    for i in range(0,4):
        f.write(str(GPD.players[i].HP) + '\n' + str(GPD.players[i].MAX_HP) + '\n')
        f.write(str(GPD.players[i].MP) + '\n' + str(GPD.players[i].MAX_MP) + '\n')
        f.write(str(GPD.players[i].LEVEL) + '\n' + str(GPD.players[i].EXP) + '\n')
        f.write(str(GPD.players[i].MAX_EXP) + '\n' + str(GPD.players[i].ATK) + '\n')
        f.write(str(GPD.players[i].DEF) + '\n' + str(GPD.players[i].AP) + '\n')

        for s in range(0,4):
            f.write(str(GPD.players[i].skill[s].POWER) + '\n')


def Load_game():
    pass