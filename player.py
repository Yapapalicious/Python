import os
from random import randint
clear = lambda: os.system('cls')

class Player(object):

    def __init__(self, name):
        self.name = name
        self.HP = 15
        self.current_HP = 15
        self.MP = 10
        self.current_MP = 10
        self.ATK = 1
        self.MATK = 1
        self.DEF = 5
        self.HIT = 5
        self.FLEE = 1
        self.gold = 10
        self.stat_points = 20
        self.inventory = [0, 0]
        self.level = 1


    def show_stats(self):
        print('Current Status Points          Status Points Remaining: {}'.format(self.stat_points))
        print('   [1] HP:      {}'.format(self.HP))
        print('   [2] MP:      {}'.format(self.MP))
        print('   [3] ATK:     {}'.format(self.ATK))
        print('   [4] MATK:    {}'.format(self.MATK))
        print('   [5] DEF:     {}'.format(self.DEF))
        print('   [6] FLEE:    {}'.format(self.FLEE))
        print('   [7] HIT:     {}'.format(self.HIT))

    def show_inventory(self):
        print('Current Inventory          Gold: {}'.format(self.gold))
        print('   [1] HP Potion    {}'.format(self.inventory[0]))
        print('   [2] MP Potion    {}'.format(self.inventory[1]))


    def allocate_stats(self):
        while self.stat_points:
            self.show_stats()
            print('   [Q] QUIT')
            print ('Available status points: {}'.format(self.stat_points))
            prompt = input('Your Choice: ')
            if prompt.isdigit():
                prompt = int(prompt)
                if prompt >= 1 and prompt <= 7:
                    choices = ['', 'HP', 'MP', 'ATK', 'MATK', 'DEF', 'FLEE', 'HIT']
                    add = int(input('How much points would you add to {}?: '.format(choices[prompt])))
                    if self.stat_points >= add:
                        if prompt == 1:
                            self.HP += int(add)
                            self.stat_points -= int(add)
                        elif prompt == 2:
                            self.MP += int(add)
                            self.stat_points -= int(add)
                        elif prompt == 3:
                            self.ATK += int(add)
                            self.stat_points -= int(add)
                        elif prompt == 4:
                            self.MATK += int(add)
                            self.stat_points -= int(add)
                        elif prompt == 5:
                            self.DEF += int(add)
                            self.stat_points -= int(add)
                        elif prompt == 6:
                            self.FLEE += int(add)
                            self.stat_points -= int(add)
                        elif prompt == 7:
                            self.HIT += int(add)
                            self.stat_points -= int(add)
                    else:
                        print('Not enough status points!')
            elif prompt.upper() == 'Q':
                break
            else:
                print('Not a valid choice!')
            clear()


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


    def get_normal_damage(self, attack_type):
        is_critical = is_critical(attack_type)
        if attack_type == 1:
            if is_critical:
                return ATK * 1.2
            else:
                return ATK
        else:
            if is_critical:
                return MATK * 1.2
            else:
                return MATK

    def get_skill_damage(self, skill_type):
        is_critical = is_critical(attack_type)
        if skill_type == 1:
            if is_critical:
                return ATK * 1.5
            else:
                return ATK
        else:
            if is_critical:
                return MATK * 1.5
            else:
                return MATK


    def use_skill(self, skill_type):
        if self.current_MP >= 3:
            self.current_MP -= 3
            return get_skill_damage(self, skill_type)
        else:
            print('Not enough MP!')
            return False


    def level_up(self):
        self.HP += randint(0, 2)
        self.MP += randint(0, 2)
        self.ATK += randint(0, 2)
        self.MATK += randint(0, 2)
        self.DEF += randint(0, 1)
        self.HIT += randint(0, 1)
        self.FLEE += randint(0, 1)
