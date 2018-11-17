from BaseItem import*
import json
import GamePlayingData as GPD

Phoenix_Down_data_file = open('json\\Item.json', 'r')
Phoenix_Down_Data = json.load(Phoenix_Down_data_file)
Phoenix_Down_data_file.close()

class PhoenixDown(Item):
    def __init__(self):
        super(PhoenixDown, self).__init__('부활의 깃털', Phoenix_Down_Data['Phoenix_Down']['NUM'], Phoenix_Down_Data['Phoenix_Down']['COST'])

    def use(self, target_index):
        GPD.players[target_index].act_type = 0
        GPD.players[target_index].HP = GPD.players[target_index].MAX_HP
        GPD.players[target_index].MP = GPD.players[target_index].MAX_MP
        print('플레이어'+str(target_index)+' 부활')
