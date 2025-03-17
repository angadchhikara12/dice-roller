import random

def roll(self=None):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    return dice1 + dice2
