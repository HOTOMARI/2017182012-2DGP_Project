import GamePlayingData as GPD


def Save_game():
    f = open('test.txt', mode='wt')
    # 캐릭터 위치
    f.write(str(GPD.now_map) + '\n' + str(int(GPD.Player.x)) + '\n' + str(int(GPD.Player.y)) + '\n')
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

    f.close()


def Load_game():
    f = open('test.txt', mode='rt')
    # 캐릭터 위치
    GPD.now_map = int(f.readline())
    GPD.x = int(f.readline())
    GPD.y = int(f.readline())
    # 아이템 정보
    GPD.money = int(f.readline())
    for i in range(0, 4):
        GPD.items[i].NUM = int(f.readline())

    # 캐릭터 정보
    for i in range(0, 4):
        GPD.players[i].HP = int(f.readline())
        GPD.players[i].MAX_HP = int(f.readline())
        GPD.players[i].MP = int(f.readline())
        GPD.players[i].MAX_MP = int(f.readline())
        GPD.players[i].LEVEL = int(f.readline())
        GPD.players[i].EXP = int(f.readline())
        GPD.players[i].MAX_EXP = int(f.readline())
        GPD.players[i].ATK = int(f.readline())
        GPD.players[i].DEF = int(f.readline())
        GPD.players[i].AP = int(f.readline())

        for s in range(0, 4):
            GPD.players[i].skill[s].POWER = int(f.readline())

    f.close()