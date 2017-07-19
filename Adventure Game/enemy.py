from random import randint
import math

class Enemy(object):

    def __init__(self, level):
        self.is_alive = True
        self.HP = 5 + randint(math.floor(level / 2), level)
        self.MP = 10 + randint(math.floor(level / 2), level)
        self.ATK = 1 + randint(math.floor(level / 2), level)
        self.MATK = 1 + randint(math.floor(level / 2), level)
        self.DEF = 2 + randint(0, math.floor(level / 2))
        self.MDEF = 2 + randint(0, math.floor(level / 2))
        self.HIT = 3 + randint(0, math.floor(level / 2))
        self.FLEE = 1 + randint(0, math.floor(level / 2))
        self.current_HP = self.HP
        self.current_MP = self.MP


    def get_damage(self):
        attack_type = randint(1, 4)
        if attack_type == 1:
            critical_strike = randint(1, 10)
            if critical_strike >= 1 and critical_strike <= 2:
                return math.ceil(self.ATK * 1.2)
            else:
                return self.ATK
        elif attack_type == 2:
            if self.current_MP >= 3:
                self.current_MP -= 3
                return math.ceil(self.ATK * 1.3)
            else:
                return self.ATK
        elif attack_type == 2:
            critical_strike = randint(1, 10)
            if critical_strike >= 1 and critical_strike <= 2:
                return math.ceil(self.MATK * 1.2)
            else:
                return self.MATK
        else:
            if self.current_MP >= 3:
                self.current_MP -= 3
                return math.ceil(self.MATK * 1.3)
            else:
                return self.MATK
