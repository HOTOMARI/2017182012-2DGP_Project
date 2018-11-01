from BaseSkill import*
import json
import Game_Playing_Data

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class Provoke(Skill):
    def __init__(self):
        super(Provoke, self).__init__('도발', Skill_Data['Provoke']['ID'], Skill_Data['Provoke']['COST'], Skill_Data['Provoke']['POWER'])

    def activate(self, my_index, target_index):
        print("도발")