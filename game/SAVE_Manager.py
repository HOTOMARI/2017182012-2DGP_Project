import Game_Playing_Data as GPD


def Save_game():
    f = open('test.txt', mode='wt')
    # 캐릭터 위치
    f.write(str(GPD.now_map) + '\n' + str(GPD.Player.x) + '\n' + str(GPD.Player.y) + '\n')
    # 캐릭터 정보
    for i in range(0,4):
        pass
    pass


def Load_game():
    pass