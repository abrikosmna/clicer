import pygame

from level_changer import LevelChanger
from boss import Boss


class Boss_menu:
    def __init__(self):
        self.bloks = []
        self.fill_boss_info()
        self.fill_level_changers()

    def fill_boss_info(self):
        for i in range(1, 5):
            self.bloks.append(Boss(i, i * 100))

    def fill_level_changers(self):
        self.bloks.insert(0, LevelChanger("left"))
        self.bloks.append(LevelChanger("right"))

    def draw_bloks(self, screen):
        for blok in self.bloks:
            blok.draw_bloks(screen)

    def change_boss_info(self, step):
        if step == -1:
            self.change_boss_info_to_the_left()
        else:
            self.change_boss_info_to_the_right()

    def change_boss_info_to_the_left(self):
        if self.bloks[1].level == 1:
            return
        self.bloks.pop(-2)
        self.bloks.insert(1, Boss(self.bloks[1].level - 1, 100))
        for i in range(2, 5):
            self.bloks[i].blok_pos[0] += 100

    def change_boss_info_to_the_right(self):
        self.bloks.pop(1)
        self.bloks.insert(-1, Boss(self.bloks[-2].level + 1, 400))
        for i in range(1, 4):
            self.bloks[i].blok_pos[0] -= 100
