from BaseItem import*
import json
import Game_Playing_Data

MP_Potion_data_file = open('json\\Item.json', 'r')
MP_Potion_Data = json.load(MP_Potion_data_file)
MP_Potion_data_file.close()

class MPpotion(Item):
    def __init__(self):
        super(MPpotion, self).__init__('에테르', MP_Potion_Data['MP_Potion']['NUM'], MP_Potion_Data['MP_Potion']['COST'])

    def use(self, target_index):
        Game_Playing_Data.players[target_index].MP += 50
        if Game_Playing_Data.players[target_index].MP > Game_Playing_Data.players[target_index].MAX_MP:
            Game_Playing_Data.players[target_index].MP = Game_Playing_Data.players[target_index].MAX_MP
        print('플레이어'+str(target_index)+'에게 MP회복 50')
        print('플레이어' + str(target_index) + 'MP: ' +
              str(Game_Playing_Data.players[target_index].MP)+'/' + str(Game_Playing_Data.players[target_index].MP))