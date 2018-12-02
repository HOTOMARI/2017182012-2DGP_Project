from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class Assassinate(Skill):
    def __init__(self):
        super(Assassinate, self).__init__('마무리 일격', Skill_Data['Assassinate']['ID'], Skill_Data['Assassinate']['COST'], Skill_Data['Assassinate']['POWER'], Skill_Data['Assassinate']['UPGRADE'])

    def activate(self, my_index, target_index):
        GPD.Battlelog.append(GPD.players[my_index].name + '의 마무리 일격')
        if GPD.monsters[target_index].HP < GPD.players[my_index].ATK:
            GPD.monsters[target_index].HP -= int((self.POWER+GPD.players[my_index].ATK) * 4)
            GPD.monsters[target_index].hate[my_index] += int(self.POWER * 2)
            GPD.Battlelog.append(GPD.players[my_index].name + '이 ' + GPD.monsters[target_index].name + '에게 ' + str(
                int((self.POWER + GPD.players[my_index].ATK) * 4)) + '피해')
        else:
            GPD.monsters[target_index].HP -= int((self.POWER+GPD.players[my_index].ATK))
            GPD.Battlelog.append(GPD.players[my_index].name + '이 ' + GPD.monsters[target_index].name + '에게 ' + str(
                int((self.POWER + GPD.players[my_index].ATK))) + '피해')
            GPD.monsters[target_index].hate[my_index] += self.POWER

        GPD.CleanLog()
