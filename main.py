import pygame
import random


class Hero:
    def __init__(self):
        self.hero = pygame.image.load("Textures/Hero.png").convert()
        self.tree = 0
        self.rock = 0
        self.count = 0
        self.name = "Nersop"
        self.lvl = 0
        self.building = False
        self.build_num = 0

    def hero_stats(self, font):
        sc.blit(self.hero, (1300, 15))
        sc.blit(font.render(self.name, True, WHITE), (1390, 17))
        sc.blit(font.render("Уровень: " + str(self.lvl), True, WHITE), (1390, 70))


def move(a):
    global stop
    desk.dsk[hero_index[0]][hero_index[1]] = 0
    s_x, s_y = hero_index[0], hero_index[1]
    if a == 1:
        c_x, c_y = pygame.mouse.get_pos()
        if 1280 > c_x - (c_x % 80) > 7 * 80 and hero_index[1] < 91:
            hero_index[1] += 1
        elif 1280 > c_x - (c_x % 80) < 7 * 80 and hero_index[1] > 0:
            hero_index[1] -= 1
        if 1280 > c_x and c_y - (c_y % 80) > 6 * 80 and hero_index[0] < 93:
            hero_index[0] += 1
        elif 1280 > c_x and c_y - (c_y % 80) < 6 * 80 and hero_index[0] > 0:
            hero_index[0] -= 1
    if a == 2:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and hero_index[1] > 0:
            hero_index[1] -= 1
        if keys[pygame.K_RIGHT] and hero_index[1] < 91:
            hero_index[1] += 1
        if keys[pygame.K_UP] and hero_index[0] > 0:
            hero_index[0] -= 1
        if keys[pygame.K_DOWN] and hero_index[0] < 93:
            hero_index[0] += 1
    if 20 <= desk.dsk[hero_index[0]][hero_index[1]] < 24:
        desk.count += 1
        if desk.count == 2:
            desk.tree += 1
            stop = 0
            desk.count = 0
        else:
            stop = 1
            hero_index[0], hero_index[1] = s_x, s_y
    else:
        stop = 0
        desk.count = 0
    if 101 <= desk.dsk[hero_index[0]][hero_index[1]] <= 102:
        if desk.dsk[hero_index[0]][hero_index[1]] == 101:
            desk.count_intfc = 2
        hero_index[0], hero_index[1] = s_x, s_y
    desk.dsk[hero_index[0]][hero_index[1]] = 1
    print(desk.count)


class Desk(Hero):
    def __init__(self, screen):
        super().__init__()
        self.dsk = [[0 for _ in range(100)] for _ in range(100)]
        self.screen = screen
        self.x, self.y = 0, 0
        self.count_intfc = 0

    def create_desk(self):
        for i in range(50):
            for j in range(random.randrange(0, 4), 50, random.randrange(3, 8)):
                a = random.randrange(0, 4)
                if a == 0:
                    self.dsk[i][j] = 20
                elif a == 1:
                    self.dsk[i][j] = 21
                elif a == 2:
                    self.dsk[i][j] = 22
                elif a == 3:
                    self.dsk[i][j] = 23
        self.dsk[hero_index[0]][hero_index[1]] = 1

    def show_desk(self):
        x, y = 0, 0
        if hero_index[1] < 92:
            for i in range(H // 80):
                a = ((hero_index[0] - 6) + i) * (((hero_index[0] - 6) + i) > 0)
                for j in range(16):
                    if self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 0:
                        self.screen.blit(grass, (x, y))
                    elif self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 1:
                        self.screen.blit(grass, (x, y))
                        self.hero.set_colorkey((255, 255, 255))
                        self.screen.blit(self.hero, (x, y))
                        self.x, self.y = a, j
                    if self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 20:
                        tree[0].set_colorkey((255, 255, 255))
                        self.screen.blit(tree[0], (x, y))
                    elif self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 21:
                        tree[1].set_colorkey((255, 255, 255))
                        self.screen.blit(tree[1], (x, y))
                    elif self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 22:
                        tree[2].set_colorkey((255, 255, 255))
                        self.screen.blit(tree[2], (x, y))
                    elif self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 23:
                        tree[3].set_colorkey((255, 255, 255))
                        self.screen.blit(tree[3], (x, y))
                    elif self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 101:
                        self.screen.blit(grass, (x, y))
                        self.screen.blit(blt_chest, (x, y))
                    elif self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 102:
                        self.screen.blit(grass, (x, y))
                        self.screen.blit(blt_wall, (x, y))
                    x += 80
                x = 0
                y += 80

    def show_interface(self):
        sc.blit(interface, (1280, 0))
        sc.blit(btn_building, (1290, 470))
        sc.blit(btn_hero, (1520, 470))
        sc.blit(btn_quit, (1290, 950))
        sc.blit(btn_save, (1290, 770))
        sc.blit(btn_load, (1290, 860))
        if self.count_intfc == 0:
            desk.hero_stats(font)
        elif self.count_intfc == 1:
            sc.blit(blt_chest, (1295, 15))
            sc.blit(blt_wall, (1375, 15))
        elif self.count_intfc == 2:
            pass
        sc.blit(count_tree, [1330, 415])
        sc.blit(count_rock, [1445, 415])


pygame.init()

W, H = 1680, 1040

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Bibus")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

FPS = 60
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

grass = pygame.image.load("Textures/TexturedGrass.png").convert()
tree1 = pygame.image.load("Textures/Tree1.png").convert()
tree2 = pygame.image.load("Textures/Tree2.png").convert()
tree3 = pygame.image.load("Textures/Tree3.png").convert()
tree4 = pygame.image.load("Textures/Tree4.png").convert()
tree = [tree1, tree2, tree3, tree4]
cursor = pygame.image.load("Textures/cursor.png").convert()
cursor.set_colorkey((255, 255, 255))
box_selector1 = pygame.image.load("Textures/BoxSelector1.png").convert()
box_selector2 = pygame.image.load("Textures/BoxSelector2.png").convert()
box_selector1.set_colorkey((255, 255, 255))
box_selector2.set_colorkey((255, 255, 255))
interface = pygame.image.load("Textures/Interface.png").convert()
btn_building = pygame.image.load("Textures/Buttons/building.png").convert()
btn_hero = pygame.image.load("Textures/Buttons/btn_hero.png").convert()
btn_quit = pygame.image.load("Textures/Buttons/quit.png").convert()
btn_load = pygame.image.load("Textures/Buttons/load.png").convert()
btn_save = pygame.image.load("Textures/Buttons/save.png").convert()
blt_chest = pygame.image.load("Textures/Building/Chests.png").convert()
blt_chest.set_colorkey((255, 255, 255))
blt_wall = pygame.image.load("Textures/Building/Wall.png").convert()
all_img = [grass, tree1, tree2, tree3, tree4, cursor, box_selector1]

font = pygame.font.Font(None, 60)
count_tree = font.render(str(Desk(sc).tree), True, WHITE)
count_rock = font.render(str(Desk(sc).rock), True, WHITE)

hero_index = [6, 7]
stop = 0

desk = Desk(sc)
desk.create_desk()

while 1:
    c_x, c_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 1660 >= c_x >= 1290 and 1024 >= c_y >= 950:
                exit()
            if not desk.building:
                move(1)
                count_tree = font.render(str(desk.tree), True, WHITE)
            if 480 < c_x < 720 and 400 < c_y < 640 and desk.building:
                if 720 > c_x - (c_x % 80) > 560 and 640 > c_y - (c_y % 80) > 480:
                    desk.dsk[hero_index[0] + 1][hero_index[1] + 1] = desk.build_num
                elif 640 > c_x - (c_x % 80) > 480 and 640 > c_y - (c_y % 80) > 480:
                    desk.dsk[hero_index[0] + 1][hero_index[1]] = desk.build_num
                elif 560 > c_x - (c_x % 80) > 400 and 640 > c_y - (c_y % 80) > 480:
                    desk.dsk[hero_index[0] + 1][hero_index[1] - 1] = desk.build_num
                elif 560 > c_x - (c_x % 80) > 400 and 560 > c_y - (c_y % 80) > 400:
                    desk.dsk[hero_index[0]][hero_index[1] - 1] = desk.build_num
                elif 560 > c_x - (c_x % 80) > 400 and 480 > c_y - (c_y % 80) > 320:
                    desk.dsk[hero_index[0] - 1][hero_index[1] - 1] = desk.build_num
                elif 640 > c_x - (c_x % 80) > 480 and 480 > c_y - (c_y % 80) > 320:
                    desk.dsk[hero_index[0] - 1][hero_index[1]] = desk.build_num
                elif 720 > c_x - (c_x % 80) > 560 and 560 > c_y - (c_y % 80) > 400:
                    desk.dsk[hero_index[0]][hero_index[1] + 1] = desk.build_num
                elif 720 > c_x - (c_x % 80) > 560 and 480 > c_y - (c_y % 80) > 320:
                    desk.dsk[hero_index[0] - 1][hero_index[1] + 1] = desk.build_num
                desk.building = False
            if desk.count_intfc == 1:
                if 1375 > c_x > 1295 and 95 > c_y > 15:
                    desk.building = True
                    desk.build_num = 101
                elif 1465 > c_x > 1375 and 95 > c_y > 15:
                    desk.building = True
                    desk.build_num = 102
            if 1437 > c_x > 1290 and 555> c_y > 470:
                desk.count_intfc = 1
            elif 1667 > c_x > 1520 and 555 > c_y > 470:
                desk.count_intfc = 0

        if event.type == pygame.KEYDOWN:
            if pygame.K_ESCAPE and desk.building:
                desk.building = False
            else:
                move(2)
                count_tree = font.render(str(desk.tree), True, WHITE)
    desk.show_desk()
    if 480 < c_x < 720 and 400 < c_y < 640:
        if stop == 0:
            sc.blit(box_selector1, (c_x - (c_x % 80), c_y - (c_y % 80)))
        else:
            sc.blit(box_selector2, (c_x - (c_x % 80), c_y - (c_y % 80)))
    desk.show_interface()
    sc.blit(cursor, (c_x, c_y))
    if desk.building:
        if c_x < 1280:
            if desk.build_num == 101:
                sc.blit(blt_chest, (c_x - (c_x % 80), c_y - (c_y % 80)))
            elif desk.build_num == 102:
                sc.blit(blt_wall, (c_x - (c_x % 80), c_y - (c_y % 80)))
    pygame.display.update()

    clock.tick(FPS)
