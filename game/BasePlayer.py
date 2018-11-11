from pico2d import*

class Player():
    def __init__(self,name,hp,maxhp,mp,maxmp,level,exp,maxexp,atk,defence,shield,ap):
        self.name = name
        self.HP = hp  # 현재 체력
        self.MAX_HP = maxhp  # 최대 체력
        self.MP = mp  # 현재 마나
        self.MAX_MP = maxmp  # 최대 마나
        self.DEF = defence  # 방어력
        self.LEVEL = level  # 레벨
        self.EXP = exp  # 현재 경험치
        self.MAX_EXP = maxexp  # 최대 경험치
        self.ATK = atk  # 공격력
        self.SHIELD = shield # 실드 전투 돌입, 종료시 0으로 초기화
        self.AP = ap # 스탯 강화용 포인트
        
        # 0 common  1 attack ready  2 attack  3 magic 4 victory 5 lesshp 6 damaged 7 die
        self.act_type=0
        self.condition = 0

    def draw(self):
        self.image.draw(self.x, self.y)