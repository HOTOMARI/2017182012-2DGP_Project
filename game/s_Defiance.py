from BaseSkill import*
import json
import Game_Playing_Data as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class Defiance(Skill):
    def __init__(self):
        super(Defiance, self).__init__('수비 태세', Skill_Data['Defiance']['ID'], Skill_Data['Defiance']['COST'], Skill_Data['Defiance']['POWER'])

    def activate(self, my_index):
        GPD.players[my_index].SHIELD += self.POWER