from BasePlayer import*
from s_GustSlash import*
from s_DeathBlossom import*
from s_Assassinate import*
from s_Diversion import*
import json
import GamePlayingData as GPD


Thief_data_file = open('json\\Player.json', 'r')
Thief_Data = json.load(Thief_data_file)
Thief_data_file.close()


class Thief(Player):
    def __init__(self,party_num):
        super(Thief, self).__init__('도적', Thief_Data['Thief']['HP'], Thief_Data['Thief']['MAX_HP'],
                                        Thief_Data['Thief']['MP'], Thief_Data['Thief']['MAX_MP'],
                                        Thief_Data['Thief']['LEVEL'], Thief_Data['Thief']['EXP'],
                                        Thief_Data['Thief']['MAX_EXP'], Thief_Data['Thief']['ATK'],
                                        Thief_Data['Thief']['DEF'],0,0)
        self.party_num = party_num
        self.frame=0
        self.attack_animation = 0
        self.anistep = 0

        # 0 common  1 attack ready  2 attack  3 magic 4 victory 5 lesshp 6 damaged 7 die
        self.act_type = 0
        self.act_type_tmp = 0

        self.status_string = self.name + '  ' + 'HP: ' + str(self.HP) + '/' + str(self.MAX_HP) + ' ' + 'MP: ' + \
                             str(self.MP) + '/' + str(self.MAX_MP)
        self.skill = [GustSlash(),DeathBlossom(),Assassinate(),Diversion()]

    def draw(self):
        if self.act_type == 0:
            GPD.Thief.image.clip_draw(0, 0, 72, 72, 600 + self.attack_animation, 420 - 75 * self.party_num)
        elif self.act_type == 1:
            GPD.Thief.image.clip_draw(72, 0, 72, 72, 600 + self.attack_animation, 420 - 75 * self.party_num)
        elif self.act_type == 2:
            GPD.Thief.image.clip_draw(144 + 72 * int(self.frame % 3), 0, 72, 72, 500, 420 - 75 * self.party_num)
        elif self.act_type == 3:
            GPD.Thief.image.clip_draw(360 + 72 * int(self.frame % 2), 0, 72, 72, 600, 410 - 75 * self.party_num)
        elif self.act_type == 4:
            if int(self.frame % 2):
                GPD.Thief.image.clip_draw(504, 0, 72, 72, 600, 420 - 75 * self.party_num)
            else:
                GPD.Thief.image.clip_draw(0, 0, 72, 72, 600 + self.attack_animation, 420 - 75 * self.party_num)
        elif self.act_type == 5:
            GPD.Thief.image.clip_draw(576, 0, 72, 72, 600, 420 - 75 * self.party_num)
        elif self.act_type == 6:
            GPD.Thief.image.clip_draw(648, 0, 72, 72, 600, 420 - 75 * self.party_num)
        elif self.act_type== 7:
            GPD.Thief.image.clip_draw(720, 0, 72, 72, 600, 420 - 75 * self.party_num)

    def renew_status(self):
        self.status_string = self.name + '  ' + 'HP: ' + str(int(self.HP)) + '/' + str(self.MAX_HP) + ' ' + 'MP: ' + \
                             str(self.MP) + '/' + str(self.MAX_MP)

    def attack(self,my_index,target_index):
        if self.ATK - self.SHIELD > 0:
            GPD.monsters[target_index].HP -= (int(self.ATK/2) - self.SHIELD)
        else:
            GPD.monsters[target_index].HP -= 1
        print(self.name + str(my_index) + '가 '+ GPD.monsters[target_index].name + str(target_index) + '를 공격')
        print(GPD.monsters[target_index].name + str(target_index) + '의 체력: ' + str(GPD.monsters[target_index].HP))
        GPD.monsters[target_index].hate[my_index] += self.ATK
