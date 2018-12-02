from BasePlayer import*
from s_Cure import*
from s_SCure import*
from s_Stone import*
from s_Protect import*
import json
import GamePlayingData as GPD


WhiteMage_data_file = open('json\\Player.json', 'r')
WhiteMage_Data = json.load(WhiteMage_data_file)
WhiteMage_data_file.close()


class WhiteMage(Player):
    def __init__(self,party_num):
        super(WhiteMage, self).__init__('백마도사', WhiteMage_Data['WhiteMage']['HP'], WhiteMage_Data['WhiteMage']['MAX_HP'],
                                        WhiteMage_Data['WhiteMage']['MP'], WhiteMage_Data['WhiteMage']['MAX_MP'],
                                        WhiteMage_Data['WhiteMage']['LEVEL'], WhiteMage_Data['WhiteMage']['EXP'],
                                        WhiteMage_Data['WhiteMage']['MAX_EXP'], WhiteMage_Data['WhiteMage']['ATK'],
                                        WhiteMage_Data['WhiteMage']['DEF'],0,0)
        self.party_num = party_num
        self.frame=0
        self.attack_animation = 0
        self.anistep = 0

        # 0 common  1 attack ready  2 attack  3 magic 4 victory 5 lesshp 6 damaged 7 die
        self.act_type = 0
        self.act_type_tmp = 0

        self.status_string = self.name + '  ' + 'HP: ' + str(self.HP) + '/' + str(self.MAX_HP) + ' ' + 'MP: ' + \
                             str(self.MP) + '/' + str(self.MAX_MP)
        self.skill = [Stone(),Cure(),SCure(),Protect()]

    def draw(self):
        if self.act_type == 0:
            GPD.WhiteMage.image.clip_draw(0, 0, 72, 72, 600 + self.attack_animation, 420 - 75 * self.party_num)
        elif self.act_type == 1:
            GPD.WhiteMage.image.clip_draw(72, 0, 72, 72, 600 + self.attack_animation, 420 - 75 * self.party_num)
        elif self.act_type == 2:
            GPD.WhiteMage.image.clip_draw(144 + 72 * int(self.frame % 3), 0, 72, 72, 500, 420 - 75 * self.party_num)
        elif self.act_type == 3:
            GPD.WhiteMage.image.clip_draw(360 + 72 * int(self.frame % 2), 0, 72, 72, 600, 410 - 75 * self.party_num)
        elif self.act_type == 4:
            if int(self.frame % 2):
                GPD.WhiteMage.image.clip_draw(504, 0, 72, 72, 600, 420 - 75 * self.party_num)
            else:
                GPD.WhiteMage.image.clip_draw(0, 0, 72, 72, 600 + self.attack_animation, 420 - 75 * self.party_num)
        elif self.act_type == 5:
            GPD.WhiteMage.image.clip_draw(576, 0, 72, 72, 600, 420 - 75 * self.party_num)
        elif self.act_type == 6:
            GPD.WhiteMage.image.clip_draw(648, 0, 72, 72, 600, 420 - 75 * self.party_num)
        elif self.act_type== 7:
            GPD.WhiteMage.image.clip_draw(720, 0, 72, 72, 600, 420 - 75 * self.party_num)

    def renew_status(self):
        self.status_string = self.name + '  ' + 'HP: ' + str(int(self.HP)) + '/' + str(self.MAX_HP) + ' ' + 'MP: ' + \
                             str(self.MP) + '/' + str(self.MAX_MP)

    def attack(self,my_index,target_index):
        if self.ATK / 2 - GPD.monsters[target_index].DEF > 0:
            dmg = int(self.ATK / 2 - GPD.monsters[target_index].DEF)
            GPD.monsters[target_index].HP -= dmg
            GPD.Battlelog.append(self.name + '가 ' + GPD.monsters[target_index].name + '에게 ' + str(dmg) + '피해')
        else:
            GPD.Battlelog.append(self.name + '의 공격이 빗나감')

        GPD.CleanLog()
