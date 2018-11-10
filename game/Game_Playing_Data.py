from pico2d import*
import overworld_charactrer

# 구별 id : 프레임 수
skill_MAXframe ={0:3, 1:19, 2:29, 11:5, 12:6, 13:24, 14:16}

players=[[]for i in range(4)]
monsters=[[]for i in range(3)]
# 체력물약 마나물약 만병통치약 불사조의 깃털
items=[[]for i in range(4)]

effects = None

money = 400
now_map = 0 #0 초원 1 던전 2 마을
x,y,bg_x,bg_y=506,1109,1600,1600

Menu = None
Ingame_font = None
Ingame_Big_font = None

Player = None
Warrior = None
WhiteMage = None
BlackMage = None
Thief = None

Attack = None
Heal = None
Raise = None
Shield = None # 각종 보호막 스킬에 돌려막기
Provoke = None
OverPower = None
Fell_Cleave = None

def Upload_data():
    global Menu, Ingame_font, Ingame_Big_font
    global Player, Warrior, WhiteMage, BlackMage, Thief
    global Attack, Heal, Raise, Provoke, OverPower, Shield, Fell_Cleave

    if Menu is None:
        Menu = Player_sound_data()
        Menu.image = load_image('image\\Menu.png')
    if Ingame_font is None:
        Ingame_font = Player_sound_data()
        Ingame_font.font = load_font('font\\H2SA1M.TTF')
    if Ingame_Big_font is None:
        Ingame_Big_font = Player_sound_data()
        Ingame_Big_font.font = load_font('font\\H2SA1M.TTF',30)

    if Player is None:
        print("로드")
        Player = overworld_charactrer.Character()
    if Warrior is None:
        Warrior = Player_sound_data()
        Warrior.image = load_image('image\\player\\Warrior.png')
    if WhiteMage is None:
        WhiteMage = Player_sound_data()
        WhiteMage.image = load_image('image\\player\\White Mage.png')
    if BlackMage is None:
        BlackMage = Player_sound_data()
        BlackMage.image = load_image('image\\player\\Black Mage.png')
    if Thief is None:
        Thief = Player_sound_data()
        Thief.image = load_image('image\\player\\Thief.png')

    if Attack is None:
        Attack = Player_sound_data()
        Attack.image = load_image('image\\effect\\Attack.png')
    if Heal is None:
        Heal = Player_sound_data()
        Heal.image = load_image('image\\effect\\Heal.png')
    if Raise is None:
        Raise = Player_sound_data()
        Raise.image = load_image('image\\effect\\Raise.png')
    if Shield is None:
        Shield = Player_sound_data()
        Shield.image = load_image('image\\effect\\Shield.png')
    if Provoke is None:
        Provoke = Player_sound_data()
        Provoke.image = load_image('image\\effect\\Provoke.png')
    if OverPower is None:
        OverPower = Player_sound_data()
        OverPower.image = load_image('image\\effect\\OverPower.png')
    if Fell_Cleave is None:
        Fell_Cleave = Player_sound_data()
        Fell_Cleave.image = load_image('image\\effect\\Fell_Cleave.png')

class Image_data():
    def __init__(self):
        self.image = None

class Player_sound_data:
    def __init__(self):
        super(Player_sound_data, self).__init__()
        self.sound = None