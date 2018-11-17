import GamePlayingData as GPD

class Effect():
    def __init__(self):
        self.frame = 0
        self.id = -1
        # 0 공격 1 힐 2 부활
        # over 10 is 플레이어 스킬

    def draw(self, my_num, party_num):
        if self.id == 0:
            GPD.Attack.image.clip_draw(0+int(self.frame % 3)*192, 0, 192, 192, 200, 410 - 100 * party_num)
        elif self.id == 1 or self.id == 16 or self.id == 17:
            GPD.Heal.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 3) - int(self.frame / 4) * 192, 192,
                                     192, 600, 420 - 75 * party_num, 72, 72)
        elif self.id == 2:
            GPD.Raise.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 5) - int(self.frame / 6) * 192, 192,
                                     192, 600, 420 - 75 * party_num, 72, 72)

        elif self.id == 11:
            GPD.Provoke.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 1) - int(self.frame / 5) * 192, 192,
                                     192, 200, 410 - 100 * party_num,128,128)

        elif self.id == 12:
            GPD.OverPower.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 1) - int(self.frame / 5) * 192, 192,
                                        192, 120, 300, 400, 300)

        elif self.id == 13:
            GPD.Defiance.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 5) - int(self.frame / 5) * 192, 192,
                                     192, 500, 420 - 75 * my_num, 100, 100)

        elif self.id == 14:
            GPD.Fell_Cleave.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 3) - int(self.frame / 5) * 192, 192,
                                        192, 200, 410 - 100 * party_num)

        elif self.id == 15:
            GPD.Stone.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 1) - int(self.frame / 5) * 192, 192,
                                        192, 200, 410 - 100 * party_num, 128, 128)

        elif self.id == 18:
            GPD.Protect.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 4) - int(self.frame / 5) * 192, 192,
                                      192, 600, 420 - 75 * 0, 72, 72)
            GPD.Protect.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 4) - int(self.frame / 5) * 192, 192,
                                        192, 500, 420 - 75 * 1, 72, 72)
            GPD.Protect.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 4) - int(self.frame / 5) * 192, 192,
                                        192, 600, 420 - 75 * 2, 72, 72)
            GPD.Protect.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 4) - int(self.frame / 5) * 192, 192,
                                        192, 600, 420 - 75 * 3, 72, 72)

        elif self.id == 19:
            GPD.Blizzard.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 4) - int(self.frame / 5) * 192, 192,
                                      192, 200, 410 - 100 * party_num, 128, 128)
        elif self.id == 20:
            GPD.SFire.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 1) - int(self.frame / 5) * 192, 192,
                                      192, 200, 300, 400, 300)
        elif self.id == 21:
            GPD.Convert.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 4) - int(self.frame / 5) * 192, 192,
                                        192, 500, 420 - 75 * 3, 72, 72)
        elif self.id == 22:
            if self.frame < 19:
                GPD.Heal.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 3) - int(self.frame / 4) * 192, 192,
                                         192, 600, 420 - 75 * party_num, 72, 72)
            GPD.Convert.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 4) - int(self.frame / 5) * 192, 192,
                                        192, 500, 420 - 75 * 3, 72, 72)
        elif self.id == 23:
            GPD.GustSlash.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 2) - int(self.frame / 5) * 192, 192,
                                         192, 200, 410 - 100 * party_num, 128, 128)

        elif self.id == 24:
            GPD.DeathBlossom.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 5) - int(self.frame / 5) * 192, 192,
                                      192, 200, 300, 400, 400)

        elif self.id == 25:
            pass

        elif self.id == 26:
            pass