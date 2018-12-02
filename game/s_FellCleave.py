from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class FellCleave(Skill):
    def __init__(self):
        super(FellCleave, self).__init__('참수', Skill_Data['FellCleave']['ID'], Skill_Data['FellCleave']['COST'], Skill_Data['FellCleave']['POWER'], Skill_Data['FellCleave']['UPGRADE'])

    def activate(self, my_index, target_index):
        GPD.Battlelog.append(GPD.players[my_index].name + '의 참수')
        GPD.players[my_index].MP -= self.COST
        GPD.monsters[target_index].HP -= int((self.POWER+GPD.players[my_index].ATK)*2)
        GPD.Battlelog.append(GPD.players[my_index].name + '가 ' + GPD.monsters[target_index].name + '에게 ' + str(
            int((self.POWER + GPD.players[my_index].ATK) * 2)) + '피해')
        GPD.monsters[target_index].hate[my_index] += self.POWER * 3
        GPD.CleanLog()
