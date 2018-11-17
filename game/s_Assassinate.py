from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class Assassinate(Skill):
    def __init__(self):
        super(Assassinate, self).__init__('마무리 일격', Skill_Data['Assassinate']['ID'], Skill_Data['Assassinate']['COST'], Skill_Data['Assassinate']['POWER'], Skill_Data['Assassinate']['UPGRADE'])

    def activate(self, my_index, target_index):
        if GPD.monsters[target_index].HP < GPD.players[my_index].ATK:
            GPD.monsters[target_index].HP -= int(self.POWER * 4)
            GPD.monsters[target_index].hate[my_index] += int(self.POWER * 2)
        else:
            GPD.monsters[target_index].HP -= int(self.POWER)
            GPD.monsters[target_index].hate[my_index] += self.POWER