from save import *
from enemy import *
from hero import *


def move(a):
    global stop
    desk.dsk[hero_index[0]][hero_index[1]] = random.randrange(11, 14)
    s_x, s_y = hero_index[0], hero_index[1]
    if a == 1:
        x, y = pygame.mouse.get_pos()
        if 1280 > x - (x % 80) > 7 * 80 and hero_index[1] < 91:
            hero_index[1] += 1
        elif 1280 > x - (x % 80) < 7 * 80 and hero_index[1] > 0:
            hero_index[1] -= 1
        if 1280 > x and y - (y % 80) > 6 * 80 and hero_index[0] < 93:
            hero_index[0] += 1
        elif 1280 > c_x and y - (y % 80) < 6 * 80 and hero_index[0] > 0:
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
    if 20 <= desk.dsk[hero_index[0]][hero_index[1]] < 24 or 30 <= desk.dsk[hero_index[0]][hero_index[1]] <= 32:
        desk.count += 1
        if desk.count == 2:
            if desk.dsk[hero_index[0]][hero_index[1]] < 24:
                desk.tree += 1
            elif desk.dsk[hero_index[0]][hero_index[1]] >= 30:
                desk.rock += 1
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
            desk.count_intfc = 4
        hero_index[0], hero_index[1] = s_x, s_y
    for i in range(len(enemy.enemies)):
        if hero_index[0] == enemy.enemies[i][1] and hero_index[1] == enemy.enemies[i][2]:
            enemy.enemies[i][4] -= 1
            if enemy.enemies[i][4] == 0:
                desk.dsk[enemy.enemies[i][1]][enemy.enemies[i][2]] = random.randrange(11, 14)
                del enemy.spis_e[enemy.spis_e.index(enemy.enemies[i][0])]
                del enemy.enemies[i]
            hero_index[0], hero_index[1] = s_x, s_y
    desk.dsk[hero_index[0]][hero_index[1]] = 1


class Desk(Hero, Enemy):
    def __init__(self, screen):
        super().__init__(sc)
        self.dsk = [[random.randrange(11, 14) for _ in range(100)] for _ in range(100)]
        self.screen = screen
        self.x, self.y = 0, 0
        self.count_intfc = 0

    def create_desk(self):
        for i in range(100):
            for j in range(random.randrange(0, 4), 100, random.randrange(3, 8)):
                b = random.randrange(0, 14)
                if b == 13:
                    self.dsk[i][j] = random.randrange(30, 33)
                else:
                    self.dsk[i][j] = random.randrange(20, 24)
        self.dsk[hero_index[0]][hero_index[1]] = 1

    def show_desk(self):
        self.dsk = enemy.dsk1
        x, y = 0, 0
        if hero_index[1] < 92:
            for i in range(H // 80):
                a = ((hero_index[0] - 6) + i) * (((hero_index[0] - 6) + i) > 0)
                for j in range(16):
                    if self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 11:
                        self.screen.blit(grass1, (x, y))
                    elif self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 12:
                        self.screen.blit(grass2, (x, y))
                    elif self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 13:
                        self.screen.blit(grass3, (x, y))
                    elif self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 1:
                        self.screen.blit(grass1, (x, y))
                        self.hero.set_colorkey((255, 255, 255))
                        self.screen.blit(self.hero, (x, y))
                        self.x, self.y = a, j
                    elif self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 20:
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
                    elif self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 30:
                        self.screen.blit(grass1, (x, y))
                        self.screen.blit(rock1, (x, y))
                    elif self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 31:
                        self.screen.blit(grass1, (x, y))
                        self.screen.blit(rock2, (x, y))
                    elif self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 32:
                        self.screen.blit(grass1, (x, y))
                        self.screen.blit(rock3, (x, y))
                    elif self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 101:
                        self.screen.blit(grass1, (x, y))
                        self.screen.blit(blt_chest, (x, y))
                    elif self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 102:
                        self.screen.blit(grass1, (x, y))
                        self.screen.blit(blt_wall, (x, y))
                    if self.dsk[hero_index[0] - 6 + i][hero_index[1] - 7 + j] == 201:
                        self.screen.blit(grass1, (x, y))
                        self.screen.blit(enemy.slime, (x, y))
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
            pygame.draw.rect(sc, (0, 200, 0), (1300, 130, 18 * desk.health, 50))
            pygame.draw.rect(sc, (0, 0, 0), (1300, 130, 360, 50), 3)
            sc.blit(font.render(str(desk.health) + " / 20", True, WHITE), (1420, 140))
            pygame.draw.rect(sc, (100, 200, 0), (1300, 190, 18 * desk.lvl, 50))
            pygame.draw.rect(sc, (0, 0, 0), (1300, 190, 360, 50), 3)
            sc.blit(font.render(str(desk.lvl) + " / 10", True, WHITE), (1420, 200))
        elif self.count_intfc == 1:
            sc.blit(blt_chest, (1295, 15))
            sc.blit(price, (1335, 90))
            sc.blit(font.render(str(5), True, WHITE), (1310, 93))
            sc.blit(blt_wall, (1375, 15))
            sc.blit(price, (1410, 100))
            sc.blit(font.render(str(8), True, WHITE), (1387, 100))
        elif self.count_intfc == 2:
            sc.blit(font.render(str("Сохранить в:"), True, WHITE), (1340, 16))
            sc.blit(save1_img, (1300, 70))
            sc.blit(save2_img, (1300, 160))
            sc.blit(save3_img, (1300, 250))
        elif self.count_intfc == 3:
            sc.blit(font.render(str("Загрузить:"), True, WHITE), (1340, 16))
            sc.blit(save1_img, (1300, 70))
            sc.blit(save2_img, (1300, 160))
            sc.blit(save3_img, (1300, 250))
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

grass1 = pygame.image.load("Textures/TexturedGrass.png").convert()
grass2 = pygame.image.load("Textures/TexturedGrass2.png").convert()
grass3 = pygame.image.load("Textures/TexturedGrass3.png").convert()
tree1 = pygame.image.load("Textures/Tree1.png").convert()
tree2 = pygame.image.load("Textures/Tree2.png").convert()
tree3 = pygame.image.load("Textures/Tree3.png").convert()
tree4 = pygame.image.load("Textures/Tree4.png").convert()
tree = [tree1, tree2, tree3, tree4]
rock1 = pygame.image.load("Textures/Rocks.png").convert()
rock1.set_colorkey((255, 255, 255))
rock2 = pygame.image.load("Textures/Rocks2.png").convert()
rock2.set_colorkey((255, 255, 255))
rock3 = pygame.image.load("Textures/Rocks3.png").convert()
rock3.set_colorkey((255, 255, 255))
rock = [rock1, rock2, rock3]
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
price = pygame.image.load("Textures/Building/Price.png").convert()
blt_chest.set_colorkey((255, 255, 255))
blt_wall = pygame.image.load("Textures/Building/Wall.png").convert()
blt_wall.set_colorkey((255, 255, 255))
save1_img = pygame.image.load("Textures/Saves/save1.png").convert()
save2_img = pygame.image.load("Textures/Saves/save2.png").convert()
save3_img = pygame.image.load("Textures/Saves/save3.png").convert()
all_img = [grass1, tree1, tree2, tree3, tree4, cursor, box_selector1]

font = pygame.font.Font(None, 60)
count_tree = font.render(str(Desk(sc).tree), True, WHITE)
count_rock = font.render(str(Desk(sc).rock), True, WHITE)

hero_index = [6, 7]
spis_e = [201]
stop = 0
s_l = 0

desk = Desk(sc)
desk.create_desk()
enemy = Enemy(desk.dsk, hero_index, sc, desk.health)

while 1:
    c_x, c_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 1660 >= c_x >= 1290 and 1024 >= c_y >= 950:
                exit()
            if 1660 >= 1290 and 844 >= c_y >= 770:
                desk.count_intfc = 2
            if 1660 >= 1290 and 934 >= c_y >= 860:
                desk.count_intfc = 3
            if 1660 >= c_x >= 1300 and 154 >= c_y >= 70:
                if desk.count_intfc == 2:
                    s = Save(1)
                    s.save(desk, hero_index, enemy)
                elif desk.count_intfc == 3:
                    s = Save(1)
                    desk.dsk[hero_index[0]][hero_index[1]] = random.randrange(11, 14)
                    desk.dsk = s.file["dsk"]
                    desk.tree = s.file["tree"]
                    desk.rock = s.file["rock"]
                    desk.name = s.file["name"]
                    desk.lvl = s.file["lvl"]
                    hero_index = s.file["hero_index"]
                    desk.health = s.file["health"]
                    enemy.enemies = s.file["enemy"]
                    enemy.spis_e = s.file["s_e"]
                    enemy = Enemy(desk.dsk, hero_index, sc, desk.health, enemy.enemies, enemy.spis_e)
                    desk.show_desk()
            elif 1660 >= c_x >= 1300 and 244 >= c_y >= 160:
                if desk.count_intfc == 2:
                    s = Save(2)
                    s.save(desk, hero_index, enemy)
                elif desk.count_intfc == 3:
                    s = Save(2)
                    desk.dsk[hero_index[0]][hero_index[1]] = random.randrange(11, 14)
                    desk.dsk = s.file["dsk"]
                    desk.tree = s.file["tree"]
                    desk.rock = s.file["rock"]
                    desk.name = s.file["name"]
                    desk.lvl = s.file["lvl"]
                    hero_index = s.file["hero_index"]
                    desk.health = s.file["health"]
                    enemy.enemies = s.file["enemy"]
                    enemy.spis_e = s.file["s_e"]
                    enemy = Enemy(desk.dsk, hero_index, sc, desk.health, enemy.enemies, enemy.spis_e)
                    desk.show_desk()
            elif 1660 >= c_x >= 1300 and 334 >= c_y >= 250:
                if desk.count_intfc == 2:
                    s = Save(3)
                    s.save(desk, hero_index, enemy)
                elif desk.count_intfc == 3:
                    s = Save(3)
                    desk.dsk[hero_index[0]][hero_index[1]] = random.randrange(11, 14)
                    desk.dsk = s.file["dsk"]
                    desk.tree = s.file["tree"]
                    desk.rock = s.file["rock"]
                    desk.name = s.file["name"]
                    desk.lvl = s.file["lvl"]
                    hero_index = s.file["hero_index"]
                    desk.health = s.file["health"]
                    enemy.enemies = s.file["enemy"]
                    enemy.spis_e = s.file["s_e"]
                    enemy = Enemy(desk.dsk, hero_index, sc, desk.health, enemy.enemies, enemy.spis_e)
                    desk.show_desk()
            if not desk.building:
                if random.randrange(1, 9) == 8:
                    enemy.spawn()
                    spis_e = enemy.spis_e
                move(1)
                enemy.e_move()
                desk.health = enemy.h_hp
                count_tree = font.render(str(desk.tree), True, WHITE)
                count_rock = font.render(str(desk.rock), True, WHITE)
            if 480 < c_x < 720 and 400 < c_y < 640 and desk.building:
                if desk.build_num == 101:
                    if desk.tree >= 5:
                        desk.tree -= 5
                    else:
                        break
                elif desk.build_num == 102:
                    if desk.tree >= 8:
                        desk.tree -= 8
                    else:
                        break
                count_tree = font.render(str(desk.tree), True, WHITE)
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
                elif 640 > c_x - (c_x % 80) > 480 > c_y - (c_y % 80) > 320:
                    desk.dsk[hero_index[0] - 1][hero_index[1]] = desk.build_num
                elif 720 > c_x - (c_x % 80) > 560 > c_y - (c_y % 80) > 400:
                    desk.dsk[hero_index[0]][hero_index[1] + 1] = desk.build_num
                elif 720 > c_x - (c_x % 80) > 560 and 480 > c_y - (c_y % 80) > 320:
                    desk.dsk[hero_index[0] - 1][hero_index[1] + 1] = desk.build_num
                desk.build_num = 0
                desk.building = False
            if desk.count_intfc == 1:
                if 1375 > c_x > 1295 and 95 > c_y > 15:
                    desk.building = True
                    desk.build_num = 101
                elif 1465 > c_x > 1375 and 95 > c_y > 15:
                    desk.building = True
                    desk.build_num = 102
            if 1437 > c_x > 1290 and 555 > c_y > 470:
                desk.count_intfc = 1
            elif 1667 > c_x > 1520 and 555 > c_y > 470:
                desk.count_intfc = 0

        if event.type == pygame.KEYDOWN:
            if pygame.K_ESCAPE and desk.building:
                desk.build_num = 0
                desk.building = False
            else:
                move(2)
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
