from BaseMonster import*
import random
import json
import Game_Playing_Data as GPD

Wolf_data_file = open('json\\Monster.json', 'r')
Wolf_Data = json.load(Wolf_data_file)
Wolf_data_file.close()

class Wolf(Monster):
    def __init__(self,party_num):
        super(Wolf, self).__init__('늑대', Wolf_Data['Wolf']['HP'], Wolf_Data['Wolf']['EXP'],
                                      Wolf_Data['Wolf']['ATK'], Wolf_Data['Wolf']['DEF'], Wolf_Data['Wolf']['MONEY'])
        self.frame=random.randint(0,3)%4
        self.party_num=party_num
        self.image=load_image('image\\monster\\monster_001.png')

        # 0 common  1 damaged 2 die
        self.act_type = 0
        self.anistep = 0

        self.condition = 0

        self.hate=[0,0,0,0]
        self.attack_target = -1

        self.die_animation = 0

    def draw(self):
        if self.act_type == 0:

            self.image.clip_draw(144*int(self.frame % 4), 0, 144, 72, 200, 410 - 100 * self.party_num, 144, 72-self.die_animation)
        elif self.act_type == 1:
            self.image.clip_draw(576 + 144*int(self.frame % 2), 0, 144, 72, 200, 410 - 100 * self.party_num)

    def attack(self,my_index):
        GPD.players[self.attack_target].SHIELD -= self.ATK
        if GPD.players[self.attack_target].SHIELD < 0:
            GPD.players[self.attack_target].HP += GPD.players[self.attack_target].SHIELD
            GPD.players[self.attack_target].SHIELD = 0

        if GPD.players[self.attack_target].HP<=0:
            GPD.players[self.attack_target].HP=0
            GPD.players[self.attack_target].act_type = 7
        elif GPD.players[self.attack_target].HP/GPD.players[self.attack_target].MAX_HP <= 0.2:
            GPD.players[self.attack_target].act_type = 5
        print('늑대' + str(my_index) + '가 '+ GPD.players[self.attack_target].name + str(self.attack_target) + '를 공격')
        print(GPD.players[self.attack_target].name + str(self.attack_target) + '의 체력: ' + str(GPD.players[self.attack_target].HP))
        
    def setting_target(self):
        global tmp, tmp_hate
        tmp, tmp_hate = -1, -1

        # 반복문 돌면서 어그로 제일 높은거 타겟
        # 같을경우 25% 확률로 타겟 변경
        for i in range(0,4):
            if GPD.players[i].HP > 0:
                if self.hate[i] > tmp_hate:
                    tmp_hate=self.hate[i]
                    tmp = i
                elif self.hate[i] == tmp_hate:
                    if random.randint(0,4) == 0:
                        tmp_hate = self.hate[i]
                        tmp = i
        self.attack_target = tmp