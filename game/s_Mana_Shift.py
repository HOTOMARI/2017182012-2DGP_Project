from BaseSkill import*
import json
import Game_Playing_Data as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class ManaShift(Skill):
    def __init__(self):
        super(ManaShift, self).__init__('마나이동', Skill_Data['Mana_Shift']['ID'], Skill_Data['Mana_Shift']['COST'], Skill_Data['Mana_Shift']['POWER'], Skill_Data['Mana_Shift']['UPGRADE'])

    def activate(self, my_index, target_index):
        GPD.players[target_index].MP += int(GPD.players[my_index].MP * 0.2)
        GPD.players[my_index].MP -= int(GPD.players[my_index].MP * 0.2)

        if GPD.players[target_index].MP > GPD.players[target_index].MAX_MP:
            GPD.players[target_index].MP = GPD.players[target_index].MAX_MP
        if GPD.players[my_index].MP < 0:
            GPD.players[my_index].MP = 0
