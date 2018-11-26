from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class Defiance(Skill):
    def __init__(self):
        super(Defiance, self).__init__('수비 태세', Skill_Data['Defiance']['ID'], Skill_Data['Defiance']['COST'], Skill_Data['Defiance']['POWER'], Skill_Data['Defiance']['UPGRADE'])

    def activate(self, my_index):
        GPD.players[my_index].SHIELD += self.POWER
        if GPD.monsters[0].name == '케프카':
            GPD.monsters[0].hate[my_index] += int(self.POWER / 3)
        else:
            for i in range(0, 3):
                GPD.monsters[i].hate[my_index] += int(self.POWER/3)