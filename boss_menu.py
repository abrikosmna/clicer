import pygame

from level_changer import LevelChanger
from boss import Boss

class Boss_menu:
    def __init__(self):
        self.bloks = []
        self.fill_boss_info()
        self.fill_level_changers()






    def fill_boss_info(self):
        for i in range(1,5):
            self.bloks.append(Boss(i, i*100))
    def fill_level_changers(self):
        self.bloks.insert(0,LevelChanger("left"))
        self.bloks.append(LevelChanger("right"))

    def draw_bloks(self, screen):
        for blok in self.bloks:
            blok.draw_bloks(screen)
