from player import Player
from enemy import Enemy
from shop import Shop

import sys
import os
import time

clear = lambda: os.system('cls')

def welcome_screen():
    print('Welcome to sapnu puas text-based adventure game')
    print('[1] Start Game')
    print('[2] Load Game')
    print('[3] Exit')
    return input('Your Choice: ')

def village_screen(name):
    print('Welcome, {}! What do you want to do?'.format(name))
    print('[1] Open Shop')
    print('[2] Enter Dungeon')
    print('[3] Save Progress')
    print('[4] Exit Game')
    return input('Your Choice: ')


def battle_screen():
    pass


def shop_screen(player):
    shop = Shop()
    shop.show_list()
    choice = input('Your Choice: ')
    if choice.isdigit():
        choice = int(choice)
        if choice >= 1 and choice <= 3:
            if shop.check_gold(player.gold, choice):
                buy_item(player, choice)




def main():
    choice = welcome_screen()
    is_alive = True

    if choice == '1':
        name = input("Enter your name: ")
        player = Player(name)
        player.allocate_stats()
    elif choice =='2':
        pass
    elif choice =='3':
        getch("Exiting.. Press any key to continue")
        EXIT()

    #while is_alive:
    choice = village_screen(player.name)
    if choice == '1':
        shop_screen(player)




main()
