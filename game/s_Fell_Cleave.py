from BaseSkill import*
import json
import Game_Playing_Data

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class Fell_Cleave(Skill):
    def __init__(self):
        super(Fell_Cleave, self).__init__('참수', Skill_Data['Fell_Cleave']['ID'], Skill_Data['Fell_Cleave']['COST'], Skill_Data['Fell_Cleave']['POWER'])

    def activate(self, my_index, target_index):
        print("참수")