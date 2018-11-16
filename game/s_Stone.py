from BaseSkill import*
import json
import Game_Playing_Data as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class Stone(Skill):
    def __init__(self):
        super(Stone, self).__init__('스톤', Skill_Data['Stone']['ID'], Skill_Data['Stone']['COST'], Skill_Data['Stone']['POWER'], Skill_Data['Stone']['UPGRADE'])

    def activate(self, my_index, target_index):
        GPD.monsters[target_index].HP -= int(self.POWER * (GPD.players[my_index].ATK / 10))
        GPD.monsters[target_index].hate[my_index] += self.POWER * 2