from random import randint
import math

class Enemy(object):

# INITIALIZE ENEMY'
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
        self.number = randint(1,4)

# RANDOMIZED; RETURNS THE ATTACK
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

# RANDOMIZE ENEMY SPRITE, ASCII
    def randomize_sprite(self, number):
        if number == 1:
            print("""
                     ,     .
                    /(     )\               A
               .--.( `.___.' ).--.         /_\\
               `._ `%_&%#%$_ ' _.'     /| <___> |\\
                  `|(@\%#%/@)|'       / (  |L|  ) \\
                   |  |%#%|  |       J d8bo|=|od8b L
                    \ \%#%/ /        | 8888|=|8888 |
                    |\|%$%|/|        J Y8P"|=|"Y8P F
                    | (.".)%|         \ (  |L|  ) /
                ___.'  `-'  `.___      \|  |L|  |/
              .'#*#`-       -'$#*`.       / )|
             /#%^#%*_ *%^%_  #  %$%\    .J (__)
             #&  . %%%#% ###%*.   *%\.-'&# (__)
             %*  J %.%#_|_#$.\J* \ %'#%*^  (__)
             *#% J %$%%#|#$#$ J\%   *   .--|(_)
             """)
        elif number == 2:
            print("""
                  -. -. `.  / .-' _.'  _
                 .--`. `. `| / __.-- _' `
                '.-.  \\  \\ |  /   _.' `_
                .-. \\  `  || |  .' _.-' `.
              .' _ \\ '  -    -'  - ` _.-.
               .' `. %%%%%   | %%%%% _.-.`-
             .' .-. ><(@)> ) ( <(@)>< .-.`.
               (("`(   -   | |   -   )'"))
              / \\\\#)\\    (.(_).)    /(#//\\
             ' / ) ((  /   | |   \\  )) (`.`.
             .'  (.) \\ .md88o88bm. / (.) \\)
               / /| / \\ `Y88888Y' / \\ | \\ \\
             .' / O  / `.   -   .' \\  O \\ \\\\
              / /(O)/ /| `.___.' | \\\\(O) \\
               / / / / |  |   |  |\\  \\  \\ \\
               / / // /|  |   |  |  \\  \\ \\
             _.--/--/'( ) ) ( ) ) )`\\-\\-\\-._
            ( ( ( ) ( ) ) ( ) ) ( ) ) ) ( ) )
            """)
        elif number == 3:
            print("""
                      __.......__
                    .-:::::::::::::-.
                  .:::''':::::::''':::.
                .:::'     `:::'     `:::.
           .'\\  ::'   ^^^  `:'  ^^^   '::  /`.
          :   \\ ::   _.__       __._   :: /   ;
         :     \\`: .' ___\     /___ `. :'/     ;
        :       /\\   (_|_)\   /(_|_)   /\\       ;
        :      / .\\   __.' ) ( `.__   /. \\      ;
        :      \\ (        {   }        ) /      ;
         :      `-(     .  ^"^  .     )-'      ;
          `.       \\  .'<`-._.-'>'.  /       .'
            `.      \\    \;`.';/    /      .'
              `._    `-._       _.-'    _.'
               .'`-.__ .'`-._.-'`. __.-'`.
             .'       `.         .'       `.
           .'           `-.   .-'           `.
            """)

        elif number == 4:
            print("""
                                                      ,--,  ,.-.
                        ,                   \\,       '-,-`,'-.' | ._
                       /|           \\    ,   |\\         }  )/  / `-,',
                       [ '          |\\  /|   | |        /  \\|  |/`  ,`
                       | |       ,.`  `,` `, | |  _,...(   (      _',
                       \\  \\  __ ,-` `  ,  , `/ |,'      Y     (   \\_L\\
                        \\  \\_\\,``,   ` , ,  /  |         )         _,/
                         \\  '  `  ,_ _`_,-,<._.<        /         /
                          ', `>.,`  `  `   ,., |_      |         /
                            \\/`  `,   `   ,`  | /__,.-`    _,   `\\
                        -,-..\\  _  \\  `  /  ,  / `._) _,-\\`       \\
                         \\_,,.) /\\    ` /  / ) (-,, ``    ,        |
                        ,` )  | \\_\\       '-`  |  `(               \\
                       /  /```(   , --, ,' \\   |`<`    ,            |
                      /  /_,--`\\   <\\  \V /> ,` )<_/)  | \\      _____)
                ,-, ,`   `   (_,\\ \\    |   /) / __/  /   `----`
               (-, \           ) \\ ('_.-._)/ /,`    /
               | /  `          `/ \\\\ V   V, /`     /
            ,--\\(        ,     <_/`\\\\     ||      /
           (   ,``-     \\/|         \-A.A-`|     /
          ,>,_ )_,..(    )\\          -,,_-`  _--`
         (_ \\|`   _,/_  /  \\_            ,--`
          \\( `   <.,../`     `-.._   _,-`
           `                      ```
            """)
