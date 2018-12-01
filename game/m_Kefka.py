from BaseMonster import *
import random
import json
import GamePlayingData as GPD

Monster_data_file = open('json\\Monster.json', 'r')
Monster_Data = json.load(Monster_data_file)
Monster_data_file.close()


class Kefka(Monster):
    sound = None
    def __init__(self, party_num):
        super(Kefka, self).__init__('케프카', Monster_Data['Kefka']['HP'], Monster_Data['Kefka']['EXP'],
                                   Monster_Data['Kefka']['ATK'], Monster_Data['Kefka']['DEF'],
                                   Monster_Data['Kefka']['MONEY'])
        self.frame = 0
        self.party_num = party_num

        self.idle = load_image('image\\monster\\Boss\\idle.png')
        self.magic_idle = load_image('image\\monster\\Boss\\magic_standby.png')
        self.attack = load_image('image\\monster\\Boss\\atk.png')
        self.lim_attack = load_image('image\\monster\\Boss\\limit_atk.png')
        self.magic_attack = load_image('image\\monster\\Boss\\magic_atk.png')

        self.f_idle = load_image('image\\monster\\Boss\\f_idle.png')
        self.f_magic_idle = load_image('image\\monster\\Boss\\f_magic_standby.png')
        self.f_attack = load_image('image\\monster\\Boss\\f_atk.png')
        self.f_lim_attack = load_image('image\\monster\\Boss\\f_limit_atk.png')
        self.f_magic_attack = load_image('image\\monster\\Boss\\f_magic_atk.png')

        if self.sound is None:
            self.sound = load_wav('sound\\fx\\KefkaLaugh.wav')

        self.magic_effect = load_image('image\\effect\\Boss_skill.png')

        # 0 common  1 attack 2 magic_ready 3 magic 4 lim_attack 5 die
        self.act_type = 0
        self.phase = 0
        # 0 common 1 fire 2 ice 3 reverseFIRE 4 reverseICE 5 Player_don't_attack->DIE 6 Player_attack->DIE
        self.next_skill = 0
        # 2 나올스킬 fire -2 나올스킬 ice
        # 플레이어는 반대로 마법 써야됨
        self.FireorIce = 0
        # 직전에 한대라도 맞았는지
        self.isDamaged = False

        self.anistep = 0

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
                                                0,'h', 400, 300, 536, 212 - self.die_animation)
                if self.frame > 30:
                    self.frame = 0
            elif self.act_type is 2:
                self.magic_idle.clip_composite_draw(int(self.frame % 3) * 61, int(89 * 3) - int(self.frame / 4) * 89, 61, 89,
                                                    0,'', 200, 300, 122, 178 - self.die_animation)
                if self.next_skill is not 0:
                    self.magic_effect.clip_draw(int(self.frame % 5) * 192, int(192 * 5) - int(192 * (self.next_skill - 1)),
                                            192, 192, 400, 300, 192, 192)
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
        elif self.phase is 1:
            if self.act_type is 0:
                self.f_idle.clip_composite_draw(int(self.frame % 3) * 127, int(147 * 3) - int(self.frame / 4) * 147, 127, 147,
                                              0,'h', 200, 370, 254, 294 - self.die_animation)
                if self.frame > 13:
                    self.frame = 0
            elif self.act_type is 1:
                self.f_attack.clip_composite_draw(int(self.frame % 3) * 313, int(147 * 9) - int(self.frame / 4) * 147, 313, 147,
                                                0,'h', 400, 370, 626, 294 - self.die_animation)
                if self.frame > 30:
                    self.frame = 0
            elif self.act_type is 2:
                self.f_magic_idle.clip_composite_draw(int(self.frame % 3) * 127, int(147 * 3) - int(self.frame / 4) * 147, 127, 147,
                                              0,'h', 200, 370, 254, 294 - self.die_animation)
                if self.next_skill is not 0:
                    self.magic_effect.clip_draw(int(self.frame % 5) * 192, int(192 * 5) - int(192 * (self.next_skill - 1)),
                                            192, 192, 400, 300, 192, 192)
                if self.frame > 13:
                    self.frame = 0
            elif self.act_type is 3:
                self.f_magic_attack.clip_composite_draw(int(self.frame % 3) * 127, int(148 * 3) - int(self.frame / 4) * 148, 127, 148,
                                              0,'h', 200, 370, 254, 296 - self.die_animation)
                if self.frame > 13:
                    self.frame = 0
            elif self.act_type is 4:
                self.f_lim_attack.clip_composite_draw(int(self.frame % 3) * 252, int(267 * 16) - int(self.frame / 4) * 267, 252, 267,
                                                    0,'h', 250, 330, 504, 534 - self.die_animation)
                if self.frame > 50:
                    self.frame = 0

    def attack_player(self):
        dmg = self.ATK

        if GPD.players[self.attack_target].SHIELD > 0:
            GPD.players[self.attack_target].SHIELD -= self.ATK
            if GPD.players[self.attack_target].SHIELD < 0:
                dmg = -GPD.players[self.attack_target].SHIELD
                GPD.players[self.attack_target].SHIELD = 0
            if dmg - GPD.players[self.attack_target].DEF > 0:
                GPD.players[self.attack_target].HP -= dmg - GPD.players[self.attack_target].DEF
                dmg = dmg - GPD.players[self.attack_target].DEF
            else:
                dmg = 0
        else:
            if dmg - GPD.players[self.attack_target].DEF > 0:
                GPD.players[self.attack_target].HP -= dmg - GPD.players[self.attack_target].DEF
                dmg = dmg - GPD.players[self.attack_target].DEF
            else:
                dmg = 0

        if GPD.players[self.attack_target].HP <= 0:
            GPD.players[self.attack_target].HP = 0
            GPD.players[self.attack_target].act_type = 7
        elif GPD.players[self.attack_target].HP / GPD.players[self.attack_target].MAX_HP <= 0.2:
            GPD.players[self.attack_target].act_type = 5

        print(self.name + '가 ' + GPD.players[self.attack_target].name + '에게 ' + str(dmg) + '만큼의 피해')

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

    def ICE(self):
        for i in range(0,4):
            if GPD.players[i].HP > 0:
                if self.next_skill is 2:
                    GPD.players[i].HP -= 1 * (-self.FireorIce)
                else:
                    GPD.players[i].HP -= 1 * (self.FireorIce)

                if GPD.players[i].HP <= 0:
                    GPD.players[i].HP = 0
                    GPD.players[i].act_type = 7
                elif GPD.players[i].HP / GPD.players[i].MAX_HP <= 0.2:
                    GPD.players[i].act_type = 5
        print('얼음!')

    def FIRE(self):
        for i in range(0,4):
            if GPD.players[i].HP > 0:
                if self.next_skill is 1:
                    GPD.players[i].HP -= 1 * (self.FireorIce)
                else:
                    GPD.players[i].HP -= 1 * (-self.FireorIce)

                if GPD.players[i].HP <= 0:
                    GPD.players[i].HP = 0
                    GPD.players[i].act_type = 7
                elif GPD.players[i].HP / GPD.players[i].MAX_HP <= 0.2:
                    GPD.players[i].act_type = 5
        print('불!')

    def EYES(self):
        for i in range(0,4):
            if GPD.players[i].HP > 0:
                if self.isDamaged is True and self.next_skill is 6:
                    GPD.players[i].HP -= 1
                elif self.isDamaged is False and self.next_skill is 5:
                    GPD.players[i].HP -= 1

                if GPD.players[i].HP <= 0:
                    GPD.players[i].HP = 0
                    GPD.players[i].act_type = 7
                elif GPD.players[i].HP / GPD.players[i].MAX_HP <= 0.2:
                    GPD.players[i].act_type = 5
        print('눈!')

    def COMMON_SKILL(self):
        if self.phase == 0:
            dmg = self.ATK

            if GPD.players[self.attack_target].SHIELD > 0:
                GPD.players[self.attack_target].SHIELD -= self.ATK
                if GPD.players[self.attack_target].SHIELD < 0:
                    dmg = -GPD.players[self.attack_target].SHIELD
                    GPD.players[self.attack_target].SHIELD = 0
                if dmg - GPD.players[self.attack_target].DEF > 0:
                    GPD.players[self.attack_target].HP -= dmg - GPD.players[self.attack_target].DEF
                    dmg = dmg - GPD.players[self.attack_target].DEF
                else:
                    dmg = 0
            else:
                if dmg - GPD.players[self.attack_target].DEF > 0:
                    GPD.players[self.attack_target].HP -= dmg - GPD.players[self.attack_target].DEF
                    dmg = dmg - GPD.players[self.attack_target].DEF
                else:
                    dmg = 0

            if GPD.players[self.attack_target].HP <= 0:
                GPD.players[self.attack_target].HP = 0
                GPD.players[self.attack_target].act_type = 7
            elif GPD.players[self.attack_target].HP / GPD.players[self.attack_target].MAX_HP <= 0.2:
                GPD.players[self.attack_target].act_type = 5

            print(self.name + '가 ' + GPD.players[self.attack_target].name + '에게 ' + str(dmg) + '만큼의 피해')

        elif self.phase == 1:
            for i in range(0, 4):
                if GPD.players[i].HP > 0:
                    GPD.players[i].HP = 1
                if GPD.players[i].HP / GPD.players[i].MAX_HP <= 0.2:
                    GPD.players[i].act_type = 5

        print('가아앙한스킬!')
        pass