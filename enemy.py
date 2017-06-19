from random import randint

class Enemy(object):

    level = 1
    def __init__(self, name):
        self.HP = 5
        self.current_HP = HP
        self.MP = 5
        self.current_MP = MP
        self.ATK = 1
        self.MATK = 1
        self.DEF = 1
        self.HIT = 3
        self.FLEE = 1

    def initialize_enemy(self):
        self.HP += randint(0, level)
        self.MP += randint(0, level)
        self.ATK += randint(0, level)
        self.MATK += randint(0, level)
        self.DEF += randint(0, level)
        self.HIT += randint(0, level)
        self.FLEE += randint(0, level)
