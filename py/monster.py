import creature
import random

class Monster(creature.Creature):
    def __init__(self):
        super().__init__(
            atk = 15,
            deff = 30,
            atk_swing = 5,
            hp = 100)
