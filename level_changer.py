import pygame.image


class LevelChanger:
    def __init__(self,arrow_type):
        self.picture = pygame.image.load(f'boss/{arrow_type}.png')
        self.step = -1 if arrow_type == "left" else 1
        self.pos = (0,0) if arrow_type == "left" else (460,0)

    def draw_bloks(self, screen):
        screen.blit(self.picture,self.pos)



