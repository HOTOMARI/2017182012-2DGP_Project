from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class Cure(Skill):
    def __init__(self):
        super(Cure, self).__init__('케알', Skill_Data['Cure']['ID'], Skill_Data['Cure']['COST'], Skill_Data['Cure']['POWER'], Skill_Data['Cure']['UPGRADE'])

    def activate(self, my_index, target_index):
        GPD.Battlelog.append(GPD.players[my_index].name + '의 케알')
        GPD.players[target_index].HP += int((self.POWER+GPD.players[my_index].DEF))
        GPD.Battlelog.append(GPD.players[target_index].name + '의 HP ' + str(int((self.POWER+GPD.players[my_index].DEF))) + '회복')
        if GPD.monsters[0].name == '케프카':
            GPD.monsters[0].hate[my_index] += (self.POWER)
        else:
            for i in range(0,3):
                GPD.monsters[i].hate[my_index] += (self.POWER)

        GPD.CleanLog()
