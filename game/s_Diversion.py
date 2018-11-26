from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class Diversion(Skill):
    def __init__(self):
        super(Diversion, self).__init__('주의전환', Skill_Data['Diversion']['ID'], Skill_Data['Diversion']['COST'], Skill_Data['Diversion']['POWER'], Skill_Data['Diversion']['UPGRADE'])

    def activate(self, my_index):
        if GPD.monsters[0].name == '케프카':
            GPD.monsters[0].hate[my_index] -= int(self.POWER * 3)
        else:
            for i in range(0, 3):
                GPD.monsters[i].hate[my_index] -= int(self.POWER*3)