import pygame.image


class LevelChanger:
    def __init__(self,arrow_type):
        self.picture = pygame.image.load(f'boss/{arrow_type}.png')
        self.step = -1 if arrow_type == "left" else 1
        self.pos = (0,0) if arrow_type == "left" else (501,0)
        self.WIDTH = 99
        self.HEIGHT = 69

    def draw_bloks(self, screen):
        screen.blit(self.picture,self.pos)

    def is_clicked(self, pos):
        return self.pos[0] < pos[0] < self.pos[0] + self.WIDTH and \
                 self.pos[1] < pos[1] < self.pos[1] + self.HEIGHT
