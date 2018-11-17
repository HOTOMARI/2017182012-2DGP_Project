from BaseSkill import*
import json
import Game_Playing_Data as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class Blizzard(Skill):
    def __init__(self):
        super(Blizzard, self).__init__('블리자드', Skill_Data['Bllizzard']['ID'], Skill_Data['Bllizzard']['COST'], Skill_Data['Bllizzard']['POWER'], Skill_Data['Bllizzard']['UPGRADE'])

    def activate(self, my_index, target_index):
        GPD.monsters[target_index].HP -= int(self.POWER * 3)
        GPD.monsters[target_index].hate[my_index] += self.POWER