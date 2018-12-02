from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class Overpower(Skill):
    def __init__(self):
        super(Overpower, self).__init__('압도', Skill_Data['Overpower']['ID'], Skill_Data['Overpower']['COST'], Skill_Data['Overpower']['POWER'], Skill_Data['Overpower']['UPGRADE'])

    def activate(self, my_index):
        GPD.Battlelog.append(self.name + '의 압도')
        for target_index in range(0,3):
            GPD.monsters[target_index].HP -= int((self.POWER+GPD.players[my_index].ATK))
            if GPD.monsters[0].name == '케프카':
                GPD.Battlelog.append(self.name + '이 ' + GPD.monsters[0].name + '에게 ' + str(
                    int((self.POWER + GPD.players[my_index].ATK))) + '피해')
                GPD.monsters[0].hate[my_index] += self.POWER * 2
            else:
                GPD.Battlelog.append(self.name + '이 ' + GPD.monsters[target_index].name + '에게 ' + str(
                    int((self.POWER + GPD.players[my_index].ATK))) + '피해')
                GPD.monsters[target_index].hate[my_index] += self.POWER * 2
            print(GPD.monsters[target_index].name + str(target_index) + '의 체력: ' + str(GPD.monsters[target_index].HP))

        GPD.CleanLog()
