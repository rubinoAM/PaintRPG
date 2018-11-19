import random
min_roll = 1
max_roll = 3

random_boost = 1 + (random.randint(min_roll,max_roll)/10)

class Secret_Boss(object):
    def __init__(self):
        self.health = 125 * random_boost
        self.power = 30 * random_boost
    def printImage(self):
        print("""
                             /\`
                            /  \`
                           |    |
                         --:'''':--
                           :'_' :
                           _:"":\___
            ' '      ____.' :::     '._
           . *=====<<=)           \    :
            .  '      '-'-'\_      /'._.'
                             \====:_ ""
                            .'     \`
                           :       :
                          /   :    \`
                         :   .      '.
                         :  : :      :
                         :__:-:__.;--'
                         '-'   '-'
        """)