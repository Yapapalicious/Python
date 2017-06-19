class Shop(object):

    def __init__(self):
        HP_potion = 5
        MP_potion = 3
        stat = 10

    def show_list(event = None):
        print("Welcome! Which do you  like to avail?")
        print('[1] (5G)  HP Potion')
        print('[1] (3G)  MP Potion')
        print('[3] (10G) Status Point')
        print('[4] Exit')

    def open_shop(event = None):
        show_list()


    def check_gold(gold, choice):
        if choice == 1:
            if gold >= 5:
                return true
        elif choice == 2:
            if gold >= 3:
                return true
        elif choice == 3:
            if gold >= 10:
                return true
        else:
            return false

    def buy_item(player, choice):
        if choice == 1:
            player.gold -= 5
            player.item[0] += 1
        elif choice == 2:
            player.gold -= 3
            player.item[1] += 1
        else:
            player.gold -= 10
            player.stat_points += 1
