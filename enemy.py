import random

from hero import *


class Enemy:
    def __init__(self, dsk1, hero_index, sc, h_hp):
        self.slime = pygame.image.load("Textures/Enemies/Slime.png")
        self.slime.set_colorkey((255, 255, 255))
        self.enemies = [[201, 3, 3, 1, 1]]
        self.spis_e = [201]
        self.dsk1 = dsk1
        self.hero_index = hero_index
        self.sc = sc
        self.h_hp = h_hp

    def spawn(self):
        enm = random.randrange(201, 210)
        x = random.randrange(0, 101)
        y = random.randrange(0, 101)
        if enm == 201:
            self.enemies.append([201, x, y, 1, 1])
        self.dsk1[x][y] = enm
        self.spis_e.append(enm)

    def e_move(self):
        for i in self.enemies:
            x_e = i[1]
            y_e = i[2]
            self.dsk1[i[1]][i[2]] = random.randrange(11, 14)
            if i[3] == 1:
                if i[1] > self.hero_index[0]:
                    i[1] -= 1
                elif i[1] < self.hero_index[0]:
                    i[1] += 1
                elif i[2] < self.hero_index[1]:
                    i[2] += 1
                elif i[2] > self.hero_index[1]:
                    i[2] -= 1
                if self.dsk1[i[1]][i[2]] == 1:
                    self.h_hp -= 1
                    i[1], i[2] = x_e, y_e
            self.dsk1[i[1]][i[2]] = i[0]
