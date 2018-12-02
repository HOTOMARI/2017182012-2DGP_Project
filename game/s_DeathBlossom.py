from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class DeathBlossom(Skill):
    def __init__(self):
        super(DeathBlossom, self).__init__('피의 비', Skill_Data['DeathBlossom']['ID'], Skill_Data['DeathBlossom']['COST'], Skill_Data['DeathBlossom']['POWER'], Skill_Data['DeathBlossom']['UPGRADE'])

    def activate(self, my_index):
        GPD.Battlelog.append(self.name + '의 피의 비')
        if GPD.monsters[0].name == '케프카':
            GPD.monsters[0].HP -= int((self.POWER+GPD.players[my_index].ATK))
            GPD.monsters[0].hate[my_index] += self.POWER * 2
            GPD.Battlelog.append(self.name + '이 ' + GPD.monsters[0].name + '에게 ' + str(
                int((self.POWER + GPD.players[my_index].ATK))) + '피해')
        else:
            for target_index in range(0,3):
                GPD.monsters[target_index].HP -= int((self.POWER+GPD.players[my_index].ATK))
                GPD.monsters[target_index].hate[my_index] += self.POWER * 2
                GPD.Battlelog.append(self.name + '이 ' + GPD.monsters[target_index].name + '에게 ' + str(
                    int((self.POWER + GPD.players[my_index].ATK))) + '피해')
        GPD.CleanLog()
