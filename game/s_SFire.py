from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class SFire(Skill):
    def __init__(self):
        super(SFire, self).__init__('파이가', Skill_Data['SFire']['ID'], Skill_Data['SFire']['COST'], Skill_Data['SFire']['POWER'], Skill_Data['SFire']['UPGRADE'])

    def activate(self, my_index):
        GPD.Battlelog.append(GPD.players[my_index].name + '의 파이가')
        GPD.players[my_index].MP -= self.COST
        if GPD.monsters[0].name == '케프카':
            GPD.monsters[0].HP -= int((self.POWER+GPD.players[my_index].ATK))
            GPD.Battlelog.append(GPD.players[my_index].name + '가 ' + GPD.monsters[0].name + '에게 ' + str(
                int((self.POWER + GPD.players[my_index].ATK))) + '피해')
            GPD.monsters[0].hate[my_index] += self.POWER * 2
            GPD.monsters[0].FireorIce = GPD.monsters[0].FireorIce - 1
        else:
            for target_index in range(0,3):
                GPD.monsters[target_index].HP -= int((self.POWER+GPD.players[my_index].ATK))
                GPD.Battlelog.append(GPD.players[my_index].name + '가 ' + GPD.monsters[target_index].name + '에게 ' + str(
                    int((self.POWER + GPD.players[my_index].ATK))) + '피해')
                GPD.monsters[target_index].hate[my_index] += self.POWER * 2
        GPD.CleanLog()
