import random

class Monster():
    _atk: int = 15
    _def: int = 30
    _atk_swing: int = 5
    _hp: int = 100

    def roll_damage(self) -> int:
        return random.randint(self._atk - self._atk_swing, self._atk + self._atk_swing)
