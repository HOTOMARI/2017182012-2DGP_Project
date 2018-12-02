from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class ManaShift(Skill):
    def __init__(self):
        super(ManaShift, self).__init__('마나이동', Skill_Data['ManaShift']['ID'], Skill_Data['ManaShift']['COST'], Skill_Data['ManaShift']['POWER'], Skill_Data['ManaShift']['UPGRADE'])

    def activate(self, my_index, target_index):
        GPD.Battlelog.append(GPD.players[my_index].name + '의 마나이동')
        GPD.Battlelog.append(GPD.players[my_index].name + '의 MP ' + str(int(GPD.players[my_index].MP * 0.2)) + '감소')
        GPD.Battlelog.append(GPD.players[my_index].name + '의 MP ' + str(int(GPD.players[my_index].MP * 0.2)) + '회복')

        GPD.players[target_index].MP += int(GPD.players[my_index].MP * 0.2)
        GPD.players[my_index].MP -= int(GPD.players[my_index].MP * 0.2)

        if GPD.players[target_index].MP > GPD.players[target_index].MAX_MP:
            GPD.players[target_index].MP = GPD.players[target_index].MAX_MP
        if GPD.players[my_index].MP < 0:
            GPD.players[my_index].MP = 0

        GPD.CleanLog()
