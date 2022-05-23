import shelve
from enemy import *


class Save:
    def __init__(self, numb):
        if numb == 1:
            self.file = shelve.open("Saves/save1")
        elif numb == 2:
            self.file = shelve.open("Saves/save2")
        elif numb == 3:
            self.file = shelve.open("Saves/save3")

    def save(self, d, i, e):
        d.dsk[i[0]][i[1]] = random.randrange(11, 14)
        self.file["dsk"] = d.dsk
        self.file["tree"] = d.tree
        self.file["rock"] = d.rock
        self.file["name"] = d.name
        self.file["lvl"] = d.lvl
        self.file["hero_index"] = i
        self.file["health"] = d.health
        self.file["enemy"] = e.enemies
        self.file["s_e"] = e.spis_e

    def __del__(self):
        self.file.close()
