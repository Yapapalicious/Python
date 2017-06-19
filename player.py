import os
from random import randint
clear = lambda: os.system('cls')

class Player(object):

    def __init__(self, name):
        self.name = name
        self.HP = 10
        self.current_HP = 10
        self.MP = 10
        self.current_MP = 10
        self.ATK = 1
        self.MATK = 1
        self.DEF = 5
        self.HIT = 5
        self.FLEE = 1
        self.gold = 10
        self.stat_points = 50
        self.inventory = [0, 0]


    def show_stats(self):
        print('Current Stat Points')
        print('   [1] HP:      {}'.format(self.HP))
        print('   [2] MP:      {}'.format(self.MP))
        print('   [3] ATK:     {}'.format(self.ATK))
        print('   [4] MATK:    {}'.format(self.MATK))
        print('   [5] DEF:     {}'.format(self.DEF))
        print('   [6] FLEE:    {}'.format(self.FLEE))
        print('   [7] HIT:     {}'.format(self.HIT))

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

    def level_up(self):
        self.HP += randint(0, 2)
        self.MP += randint(0, 2)
        self.ATK += randint(0, 2)
        self.MATK += randint(0, 2)
        self.DEF += randint(0, 1)
        self.HIT += randint(0, 1)
        self.FLEE += randint(0, 1)
