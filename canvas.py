import random
min_roll = 1
max_roll = 4

random_boost = 1 + (random.randint(min_roll,max_roll)/10)

class Canvas(object):
    def __init__(self):
        self.health = 100 * random_boost
        self.power = 20 * random_boost