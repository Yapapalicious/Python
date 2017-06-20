from player import Player
from enemy import Enemy
from shop import Shop

from random import randint

import sys
import os
import time
import math

clear = lambda: os.system('cls')

def welcome_screen():
    print('Welcome to sapnu puas text-based adventure game')
    print('    [1] Start Game')
    print('    [2] Load Game')
    print('    [3] Exit')
    return input('Your Choice: ')

def village_screen(name):
    print('Welcome, {}! What do you want to do?'.format(name))
    print('[1] Manage Character')
    print('[2] Visit Doctor')
    print('[3] Open Shop')
    print('[4] Enter Dungeon')
    print('[5] Save Progress')
    print('[Q] Exit Game')
    return input('Your Choice: ')


def is_hit(hit, flee):
    if hit >= flee:
        return True
    else:
        chance = math.ceil((hit / flee) * 100)
        if chance >= 1:
            is_hit = randint(1, chance)
            if is_hit >= math.ceil(chance / (100 / chance)):
                return True
            else:
                return False
        else:
            return False


def calculate_damage(damage, hit, subject):
    if is_hit(hit, subject.FLEE):
        subject.current_HP -= damage
    if subject.current_HP <= 0:
        subject.is_alive = False


def battle_screen(player, level):
    enemy = Enemy(level)
    while enemy.is_alive and player.is_alive:
        attack_success = False
        while attack_success != True:
            clear()
            print('Dungeon Level {}'.format(level))
            print('Your HP: {}              Enemy HP: {}'.format(player.current_HP, enemy.current_HP))
            print('Your MP: {}'.format(player.current_MP))
            print('    [1] Physical Attack      [3] Physical Skill      [5] Use HP Potion       [7] RUN!')
            print('    [2] Magical Attack       [4] Magical Skill       [6] Use MP Potion')
            choice = input('Your Choice: ')
            if choice == '1':
                damage = player.get_normal_damage(1)
                calculate_damage(damage, player.HIT, enemy)
                attack_success = True
            elif choice =='2':
                damage = player.get_normal_damage(2)
                calculate_damage(damage, player.HIT, enemy)
                attack_success = True
            elif choice == '3':
                damage = player.use_skill(1)
                if damage:
                    calculate_damage(damage, player.HIT, enemy)
                    attack_success = True
            elif choice == '4':
                damage = player.use_skill(2)
                if damage:
                    calculate_damage(damage, player.HIT, enemy)
                    attack_success = True
            elif choice == '5':
                if player.use_potion(1):
                    print('Health has been restored')
                else:
                    print('Not enough HP Potion!')
            elif choice == '6':
                if player.use_potion(2):
                    print('Mana has been restored!')
                else:
                    print('Not enough MP Potion!')


        damage = enemy.get_damage()
        if enemy.is_alive:
            calculate_damage(damage, enemy.HIT, player)
        print('Your HP: {}              Enemy HP: {}'.format(player.current_HP, enemy.current_HP))
        print('DAMAGE: {}'.format(damage))

    if player.is_alive:
        player.level_up()
        player.show_stats()
    player.gold += randint(5, 10)


def shop_screen(player):
    shop = Shop()
    shop.show_list()
    choice = input('Your Choice: ')
    if choice.isdigit():
        choice = int(choice)
        if choice >= 1 and choice <= 3:
            if shop.check_gold(player.gold, choice):
                shop.buy_item(player, choice)
                player.show_inventory()

def visit_doctor(player):
    if player.gold >= 10:
        if player.current_HP == player.HP:
            print('Health already full')
        else:
            player.current_HP = player.HP
            player.gold -= 10
            print('Health has been restored!')
    else:
        print('Not enough gold!')

def main():
    choice = welcome_screen()
    is_alive = True
    level = 1

    if choice == '1':
        name = input("Enter your name: ")
        player = Player(name)
        player.allocate_stats()
    elif choice =='2':
        pass
    elif choice =='3':
        getch("Exiting.. Press any key to continue")
        EXIT()

    while player.is_alive:
        choice = village_screen(player.name)
        if choice == '1':
            player.manage_character()
        elif choice == '2':
            visit_doctor(player)
        elif choice == '3':
            shop_screen(player)
        elif choice == '4':
            battle_screen(player, level)
            level += 1




main()
