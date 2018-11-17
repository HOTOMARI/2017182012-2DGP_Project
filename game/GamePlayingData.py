from pico2d import*
import overworld_charactrer

# 구별 id : 프레임 수
skill_MAXframe ={0: 3, 1: 19, 2: 29, 11: 15, 12: 6, 13: 24, 14: 16, 15: 6, 16: 19, 17: 19, 18: 22,
                 19: 21, 20: 10, 21: 22, 22: 22, 23: 15, 24: 28, 25: 20, 26: 26}

players=[[]for i in range(4)]
monsters=[[]for i in range(3)]
# 체력물약 마나물약 만병통치약 불사조의 깃털
items=[[]for i in range(4)]

effects = None

money = 400
now_map = 0 #0 초원 1 던전 2 마을
x, y = 506, 1109

Menu = None
Ingame_font = None
Ingame_Big_font = None

Player = None
Warrior = None
WhiteMage = None
BlackMage = None
Thief = None

Attack = None
Heal = None # 각종 힐 스킬에 돌려막기
Raise = None
Defiance = None
Provoke = None
OverPower = None
Fell_Cleave = None
Stone = None
Protect = None
Blizzard = None
SFire = None
Convert = None
GustSlash = None
DeathBlossom = None
Assassinate = None
Diversion = None

def Upload_data():
    global Menu, Ingame_font, Ingame_Big_font
    global Player, Warrior, WhiteMage, BlackMage, Thief
    global Attack, Heal, Raise, Provoke, OverPower, Defiance, Fell_Cleave, Stone, Protect
    global Blizzard, SFire, Convert, GustSlash, DeathBlossom, Assassinate, Diversion

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
        WhiteMage.image = load_image('image\\player\\WhiteMage.png')
    if BlackMage is None:
        BlackMage = Player_sound_data()
        BlackMage.image = load_image('image\\player\\BlackMage.png')
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
    if Defiance is None:
        Defiance = Player_sound_data()
        Defiance.image = load_image('image\\effect\\Shield.png')
    if Provoke is None:
        Provoke = Player_sound_data()
        Provoke.image = load_image('image\\effect\\Provoke.png')
    if OverPower is None:
        OverPower = Player_sound_data()
        OverPower.image = load_image('image\\effect\\OverPower.png')
    if Fell_Cleave is None:
        Fell_Cleave = Player_sound_data()
        Fell_Cleave.image = load_image('image\\effect\\Fell_Cleave.png')
    if Stone is None:
        Stone = Player_sound_data()
        Stone.image = load_image('image\\effect\\Stone.png')
    if Protect is None:
        Protect = Player_sound_data()
        Protect.image = load_image('image\\effect\\Protect.png')
    if Blizzard is None:
        Blizzard = Player_sound_data()
        Blizzard.image = load_image('image\\effect\\Blizzard.png')
    if SFire is None:
        SFire = Player_sound_data()
        SFire.image = load_image('image\\effect\\SFire.png')
    if Convert is None:
        Convert = Player_sound_data()
        Convert.image = load_image('image\\effect\\Convert.png')
    if GustSlash is None:
        GustSlash = Player_sound_data()
        GustSlash.image = load_image('image\\effect\\GustSlash.png')
    if DeathBlossom is None:
        DeathBlossom = Player_sound_data()
        DeathBlossom.image = load_image('image\\effect\\DeathBlossom.png')
    if Assassinate is None:
        Assassinate = Player_sound_data()
        Assassinate.image = load_image('image\\effect\\Assassinate.png')
    if Diversion is None:
        Diversion = Player_sound_data()
        Diversion.image = load_image('image\\effect\\Diversion.png')

class Image_data():
    def __init__(self):
        self.image = None

class Player_sound_data:
    def __init__(self):
        super(Player_sound_data, self).__init__()
        self.sound = None