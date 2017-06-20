from random import randint
import math

class Enemy(object):

    def __init__(self, level):
        self.is_alive = True
        self.HP = 5
        self.MP = 10
        self.ATK = 1
        self.MATK = 1
        self.DEF = 2
        self.MDEF = 2
        self.HIT = 3
        self.FLEE = 1
        multiplier = level * 2
        self.HP += randint(0, multiplier)
        self.MP += randint(0, multiplier)
        self.ATK += randint(0, multiplier)
        self.MATK += randint(0, multiplier)
        self.DEF += randint(0, multiplier)
        self.MDEF += randint(0, multiplier)
        self.HIT += randint(0, multiplier)
        self.FLEE += randint(0, multiplier)
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
