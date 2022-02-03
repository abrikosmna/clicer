import pygame
from boss_menu import Boss_menu
from level_changer import LevelChanger

class Main:

    def __init__(self):
        pygame.init()
        self.WINDOW_WIDHT = 600
        self.WINDOW_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WINDOW_WIDHT, self.WINDOW_HEIGHT))
        self.boss_menu = Boss_menu()
        self.white = [255, 255, 255]
        self.active_boss_level = 1

    def launch(self):
        while True:
            self.draw()
            self.screen.fill(self.white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.try_to_click(event.pos)

    def draw(self):
        self.boss_menu.draw_bloks(self.screen)
        pygame.display.flip()


    def try_to_click(self, pos):
        for blok in self.boss_menu.bloks:
            if blok.is_clicked(pos):
                if isinstance(blok, LevelChanger):
                    self.boss_menu.change_boss_info(blok.step)
                    break

main = Main()
main.launch()
