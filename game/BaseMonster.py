from pico2d import*

class Monster():
    def __init__(self,name,hp,exp,atk,defence,money):
        self.name = name
        self.image = load_image('image\\dummy.jpg')  # 객체의 이미지 초기화
        self.HP = hp  # 현재 체력
        self.DEF = defence  # 방어력
        self.EXP = exp  # 현재 경험치
        self.ATK = atk  # 공격력
        self.MONEY = money  # 돈

    def draw(self):
        self.image.draw(self.x, self.y)