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
        GPD.monsters[target_index].HP -= int(self.POWER * (GPD.players[my_index].ATK / 5))
        GPD.monsters[target_index].hate[my_index] += self.POWER * 3