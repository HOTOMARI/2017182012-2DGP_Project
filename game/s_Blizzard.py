from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class Blizzard(Skill):
    def __init__(self):
        super(Blizzard, self).__init__('블리자드', Skill_Data['Blizzard']['ID'], Skill_Data['Blizzard']['COST'], Skill_Data['Blizzard']['POWER'], Skill_Data['Blizzard']['UPGRADE'])

    def activate(self, my_index, target_index):
        GPD.Battlelog.append(self.name + '의 블리자드')
        if GPD.monsters[0].name == '케프카':
            GPD.monsters[0].FireorIce = GPD.monsters[0].FireorIce + 1
            GPD.monsters[0].HP -= int((self.POWER + GPD.players[my_index].ATK) * 3)
            GPD.monsters[0].hate[my_index] += self.POWER
            GPD.Battlelog.append(self.name + '이 ' + GPD.monsters[0].name + '에게 ' + str(
                int((self.POWER + GPD.players[my_index].ATK) * 3)) + '피해')
        else:
            GPD.monsters[target_index].HP -= int((self.POWER+GPD.players[my_index].ATK) * 3)
            GPD.monsters[target_index].hate[my_index] += self.POWER
            GPD.Battlelog.append(self.name + '이 ' + GPD.monsters[target_index].name + '에게 ' + str(
                int((self.POWER+GPD.players[my_index].ATK) * 3)) + '피해')

        GPD.CleanLog()
