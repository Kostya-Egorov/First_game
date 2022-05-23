import random

from hero import *


class Enemy:
    def __init__(self, dsk1=None, hero_index='', sc='', h_hp='', enem=None, s_enem=None):
        if s_enem is None:
            s_enem = []
        if enem is None:
            enem = []
        if dsk1 is None:
            dsk1 = []
        self.slime = pygame.image.load("Textures/Enemies/Slime.png")
        self.slime.set_colorkey((255, 255, 255))
        self.enemies = enem
        self.spis_e = s_enem
        self.dsk1 = dsk1
        self.hero_index = hero_index
        self.sc = sc
        self.h_hp = h_hp

    def spawn(self):
        enm = random.randrange(201, 210)
        if enm not in self.spis_e and len(self.spis_e) < 9:
            print(self.spis_e)
            self.spis_e.append(enm)
            x = random.randrange(0, 100)
            y = random.randrange(0, 100)
            if enm == 201:
                self.enemies.append([201, x, y, 1, 1])
            self.dsk1[x][y] = enm

    def e_move(self):
        for i in self.enemies:
            x_e = i[1]
            y_e = i[2]
            self.dsk1[i[1]][i[2]] = random.randrange(11, 14)
            if i[3] == 1:
                if i[1] > int(self.hero_index[0]):
                    i[1] -= 1
                elif i[1] < int(self.hero_index[0]):
                    i[1] += 1
                elif i[2] < int(self.hero_index[1]):
                    i[2] += 1
                elif i[2] > int(self.hero_index[1]):
                    i[2] -= 1
                if self.dsk1[i[1]][i[2]] not in [11, 12, 13]:
                    if i[1] > int(self.hero_index[0]) or i[1] < int(self.hero_index[0]):
                        i[1] += random.randrange(-1, 2, 1)
                    elif i[2] < int(self.hero_index[1]) or i[2] > int(self.hero_index[1]):
                        i[2] += random.randrange(-1, 2, 1)
                if self.dsk1[i[1]][i[2]] == 1:
                    self.h_hp -= 1
                    i[1], i[2] = x_e, y_e
            self.dsk1[i[1]][i[2]] = i[0]
