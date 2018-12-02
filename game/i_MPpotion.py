from BaseItem import*
import json
import GamePlayingData as GPD

MP_Potion_data_file = open('json\\Item.json', 'r')
MP_Potion_Data = json.load(MP_Potion_data_file)
MP_Potion_data_file.close()

class MPpotion(Item):
    def __init__(self):
        super(MPpotion, self).__init__('에테르', MP_Potion_Data['MP_Potion']['NUM'], MP_Potion_Data['MP_Potion']['COST'])

    def use(self, target_index):
        GPD.players[target_index].MP += 50
        if GPD.players[target_index].MP > GPD.players[target_index].MAX_MP:
            GPD.players[target_index].MP = GPD.players[target_index].MAX_MP
        while len(GPD.Battlelog) >= 5:
            GPD.Battlelog.pop()
        GPD.Battlelog.append(GPD.players[target_index].name + '의 MP 50 회복')
