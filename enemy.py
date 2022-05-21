import pygame
import random


class Enemy:
    def __init__(self, dsk1, hero_index, sc):
        self.slime = pygame.image.load("Textures/Enemies/Slime.png")
        self.slime.set_colorkey((255, 255, 255))
        self.enemies = [[201, 3, 3, 1, 1]]
        self.dsk1 = dsk1
        self.hero_index = hero_index
        self.sc = sc

    def spawn(self):
        enm = random.randrange(201, 210)
        x = random.randrange(0, 101)
        y = random.randrange(0, 101)
        if enm == 201:
            self.enemies.append([201, x, y, 1, 1])
        self.dsk1[x][y] = enm

    def e_move(self):
        for i in self.enemies:
            if i[3] == 1:
                if i[1] > self.hero_index[0]:
                    i[1] -= 1
                elif i[1] < self.hero_index[0]:
                    i[1] += 1
                elif i[2] < self.hero_index[1]:
                    i[2] += 1
                elif i[2] > self.hero_index[1]:
                    i[2] -= 1
