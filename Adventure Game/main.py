from player import Player
from enemy import Enemy
from shop import Shop

from random import randint

import sys
import os
import time
import math
import json

# CLEAR SCREEN
def clear():
    os.system('cls')

# WELCOME SCREEN, SHOWS OPTION TO EITHER START, LOAD OR EXIT
def welcome_screen():
    print('Welcome to sapnu puas text-based adventure game')
    print('    [1] Start Game')
    print('    [2] Load Game')
    print('    [3] Exit')
    return input('Your Choice: ')

# VILLAGE SCREEN, ALLOWS THE PLAYER TO CHOOSE AMONG THE FOLLOWING
def village_screen(name):
    print('Welcome, {}! What do you want to do?'.format(name))
    print('[1] Manage Character')
    print('[2] Visit Doctor')
    print('[3] Open Shop')
    print('[4] Enter Dungeon')
    print('[5] Save Progress')
    print('[Q] Exit Game')
    return input('Your Choice: ')

# RETURNS TRUE IF ATTACK HITS THE TARGET, ELSE RETURNS FALSE
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

# DEDUCTS THE DAMAGE TO THE PLAYER/ENEMY HEALTH 
def calculate_damage(damage, hit, subject):
    if is_hit(hit, subject.FLEE):
        subject.current_HP -= damage
    if subject.current_HP <= 0:
        subject.is_alive = False

# BATTLE SCREEN, ALLOWS THE PLAYER TO EITHER ATTACK, USE SKILL, OR USE POTION.
  AFTER THE PLAYER'S MOVE, ENEMY AUTOMATICALLY ATTACKS
  IF ENEMY IS KILLED, PLAYER LEVELS UP, ELSE IF PLAYER IS KILLED, GAME ENDS
def battle_screen(player, level):
    enemy = Enemy(level)
    while enemy.is_alive and player.is_alive:
        round_success = False
        while round_success != True:
            print(enemy.randomize_sprite(enemy.number
            ))
            print('Dungeon Level {}'.format(level))
            print('Your HP: {}              Enemy HP: {}'.format(player.current_HP, enemy.current_HP))
            print('Your MP: {}'.format(player.current_MP))
            print('    [1] Physical Attack      [3] Physical Skill      [5] Use HP Potion')
            print('    [2] Magical Attack       [4] Magical Skill       [6] Use MP Potion')
            choice = input('Your Choice: ')
            clear()
            if choice == '1':
                damage = player.use_physical_attack()
                calculate_damage(damage, player.HIT, enemy)
                round_success = True
            elif choice =='2':
                damage = player.use_magical_attack()
                calculate_damage(damage, player.HIT, enemy)
                round_success = True
            elif choice == '3':
                if player.check_mana():
                    calculate_damage(player.use_physical_skill(), player.HIT, enemy)
                    round_success = True
            elif choice == '4':
                if player.check_mana():
                    calculate_damage(player.use_magical_skill(), player.HIT, enemy)
                    round_success = True
            elif choice == '5':
                if player.use_hp_potion():
                    print('Health has been restored')
                    round_success = True
                else:
                    print('Not enough HP Potion!')
            elif choice == '6':
                if player.use_mp_potion():
                    print('Mana has been restored!')
                    round_success = True
                else:
                    print('Not enough MP Potion!')

        damage = enemy.get_damage()
        if enemy.is_alive:
            calculate_damage(damage, enemy.HIT, player)


    if player.is_alive:
        print('Dungeon cleared! You have just leveled up!')
        player.level_up()
        player.show_stats()
        input("Press Enter to continue...")
        clear()
    player.gold += randint(0, 5)

# SHOP SCREEN, ALLOWS THE PLAYER TO BUY POTION / STAT
def shop_screen(player):
    shop = Shop()
    shop.show_list()
    choice = input('Your Choice: ')
    clear()
    if choice.isdigit():
        choice = int(choice)
        if choice >= 1 and choice <= 3:
            if shop.check_gold(player.gold, choice):
                shop.buy_item(player, choice)
                player.show_inventory()

# ALLOWS THE PLAYER TO RESTORE HEALTH/MANA IN EXCHANGE FOR GOLD
def visit_doctor(player):
    if player.gold >= 10:
        if player.current_HP == player.HP:
            print('Health already full')
        else:
            player.current_HP = player.HP
            player.current_MP = player.MP
            player.gold -= 10
            print('Health and mana has been restored!')
    else:
        print('Not enough gold!')

# SAVE PROGRESS
def save_game(player):
    progress = player.__dict__
    data = json.dumps(progress)
    with open('saved_game.txt', 'w') as game:
        game.write(data)

# LOAD SAVED PROGRESS IF IT EXISTS
def load_game():
    if os.path.exists('saved_game.txt'):
        game = open('saved_game.txt', 'r')
        progress = game.read()
        data = json.loads(progress)
        player = Player(data['name'])
        player.__dict__ = data
        return player
    else:
        print('No game saved!')


# SAVES THE HIGHEST LEVEL
def save_highest_level(level):
    highest_level = level
    data = json.dumps(highest_level)
    with open('highest_level.txt', 'w') as score:
        score.write(data)


# LOADS THE HIGHEST LEVEL THAT WAS SAVED, EXCLUDING THE CURRENT PROGRESS
def load_highest_level():
    if os.path.exists('highest_level.txt'):
        score = open('highest_level.txt', 'r')
        highest_level = score.read()
        data = json.loads(highest_level)
        return data

# OPENING STORY
def opening_story():
    story = ["A ", "long ", "time ", "ago, ", "there ", "is ", "a ", "demon ", "who ", "has ", "done ", "nothing ", "but ", "chaos,", " and ", "destroying ", "everything ", "it ", "sees. "]

    for i in range(len(story)):
        sys.stdout.write(story[i])
        sys.stdout.flush()
        time.sleep(0.1)
    input('\n\n\n\nPress any key to continue...')
    clear()


# MAIN SCREEN
def main():
    clear()
    highest_level = 1
    while True:
        choice = welcome_screen()
        clear()
        if choice == '1':
            opening_story()
            name = input("Enter your name: ")
            player = Player(name)
            player.allocate_stats()
            break
        elif choice =='2':
            player = load_game()
            highest_level = load_highest_level()
            if player != None:
                break
        elif choice =='3':
            sys.exit()

    while player.is_alive:
        choice = village_screen(player.name)
        clear()
        if choice == '1':
            player.manage_character()
        elif choice == '2':
            visit_doctor(player)
        elif choice == '3':
            shop_screen(player)
        elif choice == '4':
            battle_screen(player, player.level)
        elif choice == '5':
            save_game(player)
        elif choice == 'Q':
            sys.exit()

    if player.level >= highest_level:
        save_highest_level(highest_level)


# EXECUTE MAIN METHOD
main()
