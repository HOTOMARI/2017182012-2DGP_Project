from BaseItem import*
import json
import GamePlayingData as GPD

Cure_Potion_data_file = open('json\\Item.json', 'r')
Cure_Potion_Data = json.load(Cure_Potion_data_file)
Cure_Potion_data_file.close()

class Curepotion(Item):
    def __init__(self):
        super(Curepotion, self).__init__('만병통치약', Cure_Potion_Data['Cure_Potion']['NUM'], Cure_Potion_Data['Cure_Potion']['COST'])

    def use(self, target_index):
        GPD.players[target_index].condition = 0
        print('플레이어'+str(target_index)+'의 상태이상 제거')