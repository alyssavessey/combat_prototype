import random

class Creature():
    _atk: int = 0
    _def: int = 0
    _atk_swing: int = 2
    _hp: int = 0
    _mp: int = 0

    def __init__(self, atk: int, deff: int, atk_swing: int, hp: int, mp: int):
        self._atk = atk
        self._def = deff
        self._atk_swing = atk_swing
        self._hp = hp
        self._mp = mp

    def is_alive(self) -> bool:
        return self._hp > 0

    def roll_damage(self, defense: int) -> int:
        swing: int = random.randint(-self._atk_swing, self._atk_swing)
        pure_damage: int = 2 * self._atk - defense
        damage: int = pure_damage + swing
        if damage <= 0:
            damage = 1
        return damage
