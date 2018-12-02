from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class Stone(Skill):
    def __init__(self):
        super(Stone, self).__init__('스톤', Skill_Data['Stone']['ID'], Skill_Data['Stone']['COST'], Skill_Data['Stone']['POWER'], Skill_Data['Stone']['UPGRADE'])

    def activate(self, my_index, target_index):
        GPD.Battlelog.append(GPD.players[my_index].name + '의 스톤')
        GPD.monsters[target_index].HP -= int((self.POWER+GPD.players[my_index].ATK))
        GPD.Battlelog.append(GPD.players[my_index].name + '가 ' + GPD.monsters[target_index].name + '에게 ' + str(
            int((self.POWER + GPD.players[my_index].ATK))) + '피해')
        GPD.monsters[target_index].hate[my_index] += self.POWER

        GPD.CleanLog()
