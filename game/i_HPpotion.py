from BaseItem import*
import json
import Game_Playing_Data

HP_Potion_data_file = open('json\\Item.json', 'r')
HP_Potion_Data = json.load(HP_Potion_data_file)
HP_Potion_data_file.close()

class HPpotion(Item):
    def __init__(self):
        super(HPpotion, self).__init__('포션', HP_Potion_Data['HP_Potion']['NUM'], HP_Potion_Data['HP_Potion']['COST'])

    def use(self, target_index):
        Game_Playing_Data.players[target_index].HP += 50
        if Game_Playing_Data.players[target_index].HP > Game_Playing_Data.players[target_index].MAX_HP:
            Game_Playing_Data.players[target_index].HP = Game_Playing_Data.players[target_index].MAX_HP
        print('플레이어'+str(target_index)+'에게 HP회복 50')
        print('플레이어' + str(target_index) + 'HP: ' +
              str(Game_Playing_Data.players[target_index].HP)+'/' + str(Game_Playing_Data.players[target_index].HP))

