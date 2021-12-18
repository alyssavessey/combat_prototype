import random

class Creature():
    _atk: int = 0
    _def: int = 0
    _atk_swing: int = 5
    _hp: int = 0

    def __init__(self, atk: int, deff: int, atk_swing: int, hp: int):
        self._atk = atk
        self._def = deff
        self._atk_swing = atk_swing
        self._hp = hp

    def is_alive(self) -> bool:
        return self._hp > 0

    def roll_damage(self) -> int:
        return random.randint(self._atk - self._atk_swing, self._atk + self._atk_swing)
