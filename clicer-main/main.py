import pygame
from boss import Boss
from boss_menu import Boss_menu
from level_changer import LevelChanger


class Main:



    def __init__(self):

        pygame.init()
        self.WINDOW_WIDHT = 600
        self.WINDOW_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WINDOW_WIDHT, self.WINDOW_HEIGHT))
        self.boss_menu = Boss_menu()
        self.active_boss_level = 1
        self.boss = Boss(self.active_boss_level,100)
        self.white = [255, 255, 255]
        self.boss_pos = (220,320)


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
                    self.try_to_click_boss(event.pos)

    def draw(self):
        self.boss_menu.draw_bloks(self.screen)
        self.boss.draw_boss(self.screen)
        self.boss.hp_boss(self.active_boss_level, self.screen)
        pygame.display.flip()


    def try_to_click(self, pos):
        for blok in self.boss_menu.bloks:
            if blok.is_clicked(pos):
                if isinstance(blok, LevelChanger):
                    self.boss_menu.change_boss_info(blok.step)
                    break

    def try_to_click_boss(self, pos):
        if boss.is_clicked_boss(pos):
            if isinstance(boss, Boss):
                self.boss.atack(self.active_boss_level)
                break


main = Main()
main.launch()
