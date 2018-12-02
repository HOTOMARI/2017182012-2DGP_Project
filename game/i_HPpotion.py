from BaseItem import*
import json
import GamePlayingData as GPD

HP_Potion_data_file = open('json\\Item.json', 'r')
HP_Potion_Data = json.load(HP_Potion_data_file)
HP_Potion_data_file.close()

class HPpotion(Item):
    def __init__(self):
        super(HPpotion, self).__init__('포션', HP_Potion_Data['HP_Potion']['NUM'], HP_Potion_Data['HP_Potion']['COST'])

    def use(self, target_index):
        GPD.players[target_index].HP += 50
        if GPD.players[target_index].HP > GPD.players[target_index].MAX_HP:
            GPD.players[target_index].HP = GPD.players[target_index].MAX_HP

        GPD.Battlelog.append(GPD.players[target_index].name + '의 HP 50 회복')
        GPD.CleanLog()

