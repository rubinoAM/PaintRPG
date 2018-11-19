import random
min_roll = 1
max_roll = 4

random_boost = 1 + (random.randint(min_roll,max_roll)/10)

class Player(object):
    def __init__(self, name):
        self.name = name
        self.health = 100 * random_boost
        self.power = 15 * random_boost
        self.laziness = 0