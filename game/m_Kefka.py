from BaseMonster import *
import random
import json
import GamePlayingData as GPD

Monster_data_file = open('json\\Monster.json', 'r')
Monster_Data = json.load(Monster_data_file)
Monster_data_file.close()


class Kefka(Monster):
    def __init__(self, party_num):
        super(Kefka, self).__init__('케프카', Monster_Data['Kefka']['HP'], Monster_Data['Kefka']['EXP'],
                                   Monster_Data['Kefka']['ATK'], Monster_Data['Kefka']['DEF'],
                                   Monster_Data['Kefka']['MONEY'])
        self.frame = random.randint(0, 3) % 4
        self.party_num = party_num

        self.idle = load_image('image\\monster\\Boss\\idle.png')
        self.magic_idle = load_image('image\\monster\\Boss\\magic_standby.png')
        self.attack = load_image('image\\monster\\Boss\\atk.png')
        self.lim_attack = load_image('image\\monster\\Boss\\limit_atk.png')
        self.magic_attack = load_image('image\\monster\\Boss\\magic_atk.png')

        # 0 common  1 attack 2 magic_ready 3 magic 4 lim_attack 5 die
        self.act_type = 0
        self.phase = 0
        self.anistep = 0

        self.condition = 0

        self.hate = [0, 0, 0, 0]
        self.attack_target = -1

        self.die_animation = 0

    def draw(self):
        if self.phase is 0:
            if self.act_type is 0:
                self.idle.clip_composite_draw(int(self.frame % 3) * 74, int(91 * 3) - int(self.frame / 4) * 91, 74, 91,
                                              0,'h', 200, 300, 148, 182 - self.die_animation)
                if self.frame > 13:
                    self.frame = 0
            elif self.act_type is 1:
                self.attack.clip_composite_draw(int(self.frame % 3) * 268, int(106 * 9) - int(self.frame / 4) * 106, 268, 106,
                                                0,'h', 200, 300, 536, 212 - self.die_animation)
                if self.frame > 30:
                    self.frame = 0
            elif self.act_type is 2:
                self.magic_idle.clip_composite_draw(int(self.frame % 3) * 61, int(89 * 3) - int(self.frame / 4) * 89, 61, 89,
                                                    0,'h', 200, 300, 122, 178 - self.die_animation)
                if self.frame > 13:
                    self.frame = 0
            elif self.act_type is 3:
                self.magic_attack.clip_composite_draw(int(self.frame % 3) * 61, int(89 * 3) - int(self.frame / 4) * 89, 61, 89,
                                                      0,'h', 200, 300, 122, 178 - self.die_animation)
                if self.frame > 13:
                    self.frame = 0
            elif self.act_type is 4:
                self.lim_attack.clip_composite_draw(int(self.frame % 3) * 261, int(298 * 16) - int(self.frame / 4) * 298, 261, 298,
                                                    0,'h', 250, 330, 522, 596 - self.die_animation)
                if self.frame > 50:
                    self.frame = 0

    def attack(self, my_index):
        GPD.players[self.attack_target].SHIELD -= self.ATK
        if GPD.players[self.attack_target].SHIELD < 0:
            GPD.players[self.attack_target].HP += GPD.players[self.attack_target].SHIELD
            GPD.players[self.attack_target].SHIELD = 0

        if GPD.players[self.attack_target].HP <= 0:
            GPD.players[self.attack_target].HP = 0
            GPD.players[self.attack_target].act_type = 7
        elif GPD.players[self.attack_target].HP / GPD.players[self.attack_target].MAX_HP <= 0.2:
            GPD.players[self.attack_target].act_type = 5
        print(
            self.name + str(my_index) + '가 ' + GPD.players[self.attack_target].name + str(self.attack_target) + '를 공격')
        print(GPD.players[self.attack_target].name + str(self.attack_target) + '의 체력: ' + str(
            GPD.players[self.attack_target].HP))

    def setting_target(self):
        global tmp, tmp_hate
        tmp, tmp_hate = -1, -1

        # 반복문 돌면서 어그로 제일 높은거 타겟
        # 같을경우 25% 확률로 타겟 변경
        for i in range(0, 4):
            if GPD.players[i].HP > 0:
                if self.hate[i] > tmp_hate:
                    tmp_hate = self.hate[i]
                    tmp = i
                elif self.hate[i] == tmp_hate:
                    if random.randint(0, 4) == 0:
                        tmp_hate = self.hate[i]
                        tmp = i
        self.attack_target = tmp