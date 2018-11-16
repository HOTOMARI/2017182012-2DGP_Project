from BaseSkill import*
import json
import Game_Playing_Data as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class SCure(Skill):
    def __init__(self):
        super(SCure, self).__init__('케알가', Skill_Data['SCure']['ID'], Skill_Data['SCure']['COST'], Skill_Data['SCure']['POWER'], Skill_Data['SCure']['UPGRADE'])

    def activate(self, my_index):
        for i in range(0, 4):
            GPD.players[i].HP += int(self.POWER * GPD.players[my_index].ATK)
        for i in range(0, 3):
            GPD.monsters[i].hate[my_index] += (self.POWER * GPD.players[my_index].ATK)