from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class GustSlash(Skill):
    def __init__(self):
        super(GustSlash, self).__init__('돌풍베기', Skill_Data['GustSlash']['ID'], Skill_Data['GustSlash']['COST'], Skill_Data['GustSlash']['POWER'], Skill_Data['GustSlash']['UPGRADE'])

    def activate(self, my_index, target_index):
        GPD.monsters[target_index].HP -= int((self.POWER+GPD.players[my_index].ATK))
        GPD.monsters[target_index].hate[my_index] += self.POWER