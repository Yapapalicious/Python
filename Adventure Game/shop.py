class Shop(object):

    def __init__(self):
        HP_potion = 5
        MP_potion = 3
        stat = 10

    def show_list(self):
        print("Welcome! Which do you  like to avail?")
        print('    [1] (5G)  HP Potion')
        print('    [2] (3G)  MP Potion')
        print('    [3] (10G) Status Point')
        print('    [4] Exit')


    def open_shop(self):
        self.show_list()


    def check_gold(self, gold, choice):
        if choice == 1:
            if gold >= 5:
                return True
        elif choice == 2:
            if gold >= 3:
                return True
        elif choice == 3:
            if gold >= 10:
                return True
        else:
            return False


    def buy_item(self, player, choice):
        if choice == 1:
            player.gold -= 5
            player.inventory[0] += 1
            print('HP Potion added!')
        elif choice == 2:
            player.gold -= 3
            player.inventory[1] += 1
            print('MP Potion added!')
        else:
            player.gold -= 10
            player.stat_points += 1
            print('Status Point added!')
