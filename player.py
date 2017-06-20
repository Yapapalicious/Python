import os
import math
from random import randint
clear = lambda: os.system('cls')

class Player(object):

    def __init__(self, name):
        self.is_alive = True
        self.name = name
        self.HP = 15
        self.current_HP = self.HP
        self.MP = 10
        self.current_MP = self.MP
        self.ATK = 1
        self.MATK = 1
        self.DEF = 5
        self.MDEF = 5
        self.HIT = 5
        self.FLEE = 1
        self.gold = 10
        self.stat_points = 20
        self.inventory = [0, 0]


    def show_stats(self):
        print('Current Status Points          Status Points Remaining: {}'.format(self.stat_points))
        print('   [1] HP:      {}'.format(self.HP))
        print('   [2] MP:      {}'.format(self.MP))
        print('   [3] ATK:     {}'.format(self.ATK))
        print('   [4] MATK:    {}'.format(self.MATK))
        print('   [5] DEF:     {}'.format(self.DEF))
        print('   [6] MDEF:    {}'.format(self.MDEF))
        print('   [7] FLEE:    {}'.format(self.FLEE))
        print('   [8] HIT:     {}'.format(self.HIT))

    def show_inventory(self):
        print('Current Inventory          Gold: {}'.format(self.gold))
        print('   [1] HP Potion    {}'.format(self.inventory[0]))
        print('   [2] MP Potion    {}'.format(self.inventory[1]))


    def allocate_stats(self):
        while self.stat_points:
            self.show_stats()
            print('   [Q] QUIT')
            prompt = input('Your Choice: ')
            if prompt.isdigit():
                prompt = int(prompt)
                if prompt >= 1 and prompt <= 8:
                    choices = ['', 'HP', 'MP', 'ATK', 'MATK', 'DEF', 'MDEF', 'FLEE', 'HIT']
                    add = int(input('How much points would you add to {}?: '.format(choices[prompt])))
                    if self.stat_points >= add and add >= 0:
                        if prompt == 1:
                            self.HP += add
                            self.stat_points -= add
                        elif prompt == 2:
                            self.MP += add
                            self.stat_points -= add
                        elif prompt == 3:
                            self.ATK += add
                            self.stat_points -= add
                        elif prompt == 4:
                            self.MATK += add
                            self.stat_points -= add
                        elif prompt == 5:
                            self.DEF += add
                            self.stat_points -= add
                        elif prompt == 6:
                            self.MDEF += add
                            self.stat_points -= add
                        elif prompt == 7:
                            self.FLEE += add
                            self.stat_points -= add
                        elif prompt == 8:
                            self.HIT += add
                            self.stat_points -= add
                    else:
                        if add < 0:
                            print('Cannot add negative status points!')
                        else:
                            print('Not enough status points!')
            elif prompt.upper() == 'Q':
                break
            else:
                print('Not a valid choice!')


    def manage_character(self):
        print('    [1] Show Inventory')
        print('    [2] Allocate Status Points')
        print('    [Q] Go back')
        choice = input('Your Choice: ')
        if choice == '1':
            self.show_inventory()
        elif choice == '2':
            self.allocate_stats()
        else:
            print('Invalid Choice')

    @staticmethod
    def is_critical(type):
            critical_strike = randint(1, 10)
            if type == 1:
                if critical_strike >= 1 and critical_strike <= 2:
                    return True
                else:
                    return False
            else:
                if critical_strike == 1:
                    return True
                else:
                    return False


    def get_skill_damage(self, skill_type):
        if skill_type == 1:
            if self.is_critical(skill_type):
                return math.ceil(self.ATK * 2)
            else:
                return math.ceil(self.ATK * 2)
        else:
            if is_critical(skill_type):
                return math.ceil(self.MATK * 1.5)
            else:
                return math.ceil(self.MATK * 1.5)


    def use_skill(self, skill_type):
        if self.current_MP >= 3:
            self.current_MP -= 3
            return self.get_skill_damage(skill_type)
        else:
            print('Not enough MP!')
            return False


    def get_normal_damage(self, attack_type):
        if attack_type == 1:
            if self.is_critical(attack_type):
                return math.ceil(self.ATK * 1.2)
            else:
                return self.ATK
        else:
            if self.is_critical(attack_type):
                return math.ceil(self.MATK * 1.2)
            else:
                return self.MATK
    def use_potion(self, potion_type):
        if potion_type == 1:
            if self.inventory[0] > 0:
                self.current_HP += 20
                if self.current_HP > self.HP:
                    self.current_HP = self.HP
                self.inventory[0] -= 1
                return True
            else:
                return False
        else:
            if self.inventory[1] > 0:
                self.current_MP += 20
                if self.current_MP > self.MP:
                    self.current_MP = self.MP
                self.inventory[0] -= 1
                return True
            else:
                return False

    def level_up(self):
        self.HP += randint(0, 3)
        self.MP += randint(0, 3)
        self.ATK += randint(0, 3)
        self.MATK += randint(0, 3)
        self.DEF += randint(0, 2)
        self.MDEF += randint(0, 2)
        self.HIT += randint(0, 2)
        self.FLEE += randint(0, 2)
        self.stat_points += randint(0, 5)
