import pygame.image


class Boss:
    def __init__(self, level, blok_pos):
        self.level = level
        self.hp = level * 100
        self.aurum = level ** 2

        self.font = pygame.font.SysFont("arial", 30)
        self.blok_picture = self.font.render(str(level), False, (0, 0, 255))
        self.blok_pos = [blok_pos + 45, 30]

        self.picture = pygame.image.load('boss\\boss.jfif')
        self.pos = (100, 100)
        self.boss_WIDTH = 220
        self.boss_HEIGHT = 320
        self.pos_boss = (220, 320)

    def draw_bloks(self, screen):
        screen.blit(self.blok_picture, self.blok_pos)

    def is_clicked(self, pos):
        return False

    def draw_boss(self, screen):
        screen.blit(self.picture, (300, 120))

    def hp_boss(self, hp, screen):
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render("HP  " + str(self.hp), True,
                          (0, 0, 0))
        screen.blit(text1, (360, 500))

    def is_clicked_boss(self,pos_boss):
        return self.pos_boss[0] < pos_boss[0] < self.pos_boss[0] + self.boss_WIDTH and \
               self.pos_boss[1] < pos_boss[1] < self.pos_boss[1] + self.boss_HEIGHT

    def atack(self, hp):
        if self.hp == 0:
            self.level += 1
            self.aurum += self.level ** 2
            print(12345)
        if self.is_clicked_boss():
            self.hp -= 1
        return self.hp
