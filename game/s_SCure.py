from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class SCure(Skill):
    def __init__(self):
        super(SCure, self).__init__('케알가', Skill_Data['SCure']['ID'], Skill_Data['SCure']['COST'], Skill_Data['SCure']['POWER'], Skill_Data['SCure']['UPGRADE'])

    def activate(self, my_index):
        GPD.Battlelog.append(GPD.players[my_index].name + '의 케알가')
        GPD.players[my_index].MP -= self.COST
        for i in range(0, 4):
            GPD.players[i].HP += int(self.POWER * GPD.players[my_index].DEF)
            GPD.Battlelog.append(GPD.players[i].name + '의 HP ' + str(int((self.POWER + GPD.players[my_index].DEF))) + '회복')
            if GPD.players[i].HP > GPD.players[i].MAX_HP:
                GPD.players[i].HP = GPD.players[i].MAX_HP
        if GPD.monsters[0].name == '케프카':
            GPD.monsters[0].hate[my_index] += (self.POWER * GPD.players[my_index].ATK)
        else:
            for i in range(0, 3):
                GPD.monsters[i].hate[my_index] += (self.POWER * GPD.players[my_index].ATK)
        GPD.CleanLog()
