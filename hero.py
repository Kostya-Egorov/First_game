import pygame


class Hero:
    def __init__(self, sc):
        self.sc = sc
        self.hero = pygame.image.load("Textures/Hero.png").convert()
        self.tree = 8
        self.rock = 0
        self.count = 0
        self.name = "Nersop"
        self.lvl = 0
        self.health = 20
        self.building = False
        self.build_num = 0

    def hero_stats(self, font):
        self.sc.blit(self.hero, (1300, 15))
        self.sc.blit(font.render(self.name, True, (255, 255, 255)), (1390, 17))
        self.sc.blit(font.render("Уровень: " + str(self.lvl), True, (255, 255, 255)), (1390, 70))
