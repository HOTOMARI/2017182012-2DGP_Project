from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class Provoke(Skill):
    def __init__(self):
        super(Provoke, self).__init__('도발', Skill_Data['Provoke']['ID'], Skill_Data['Provoke']['COST'], Skill_Data['Provoke']['POWER'], Skill_Data['Provoke']['UPGRADE'])

    def activate(self, my_index, target_index):
        if GPD.monsters[0].name is '케프카':
            GPD.monsters[0].hate[my_index] = GPD.monsters[0].hate[my_index] + (self.POWER * 10)
        else:
            max_value = -1
            for player in range(0,3):
                if GPD.monsters[target_index].hate[player] > max_value:
                    max_value = GPD.monsters[target_index].hate[player]

            GPD.monsters[target_index].hate[my_index] = max_value + (self.POWER*10)