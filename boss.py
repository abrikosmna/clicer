import pygame.image


class Boss:
    def __init__(self, level, blok_pos):
        self.level = level
        self.hp = level*100
        self.aurum = level**2


        self.font = pygame.font.SysFont("arial", 30)
        self.blok_picture = self.font.render(str(level), False, (0,0,255))
        self.blok_pos = (blok_pos + 30, 30)

        self.picture = pygame.image.load("boss/boss.jfif")
        self.pos = (100,100)

    def draw_bloks(self, screen):
        screen.blit(self.blok_picture,self.blok_pos)