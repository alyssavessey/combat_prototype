import random

class Player():
    _MIN_ATK_GAIN: int = 2
    _MAX_ATK_GAIN: int = 3
    _MIN_DEF_GAIN: int = 2
    _MAX_DEF_GAIN: int = 3
    _MIN_HP_GAIN: int = 5
    _MAX_HP_GAIN: int = 9
    _MIN_MP_GAIN: int = 2
    _MAX_MP_GAIN: int = 4

    _level: int = 0
    _atk: int = 0
    _def: int = 0
    _max_hp: int = 0
    _max_mp: int = 0
    _hp: int = 0

    _atk_swing: int = 5

    def __init__(self, level: int) -> None:
        self._level = level
        for i in range(1, self._level + 1):
            self._atk += random.randint(self._MIN_ATK_GAIN, self._MAX_ATK_GAIN)
            self._def += random.randint(self._MIN_DEF_GAIN, self._MAX_DEF_GAIN)
            self._max_hp += random.randint(self._MIN_HP_GAIN, self._MAX_HP_GAIN)
            self._max_mp += random.randint(self._MIN_MP_GAIN, self._MAX_HP_GAIN)
        self._hp = self._max_hp

    def __str__(self) -> str:
        s: str = ""
        s += "ATK: " + str(self._atk) + "\n"
        s += "DEF: " + str(self._def) + "\n"
        s += "MAX_HP: " + str(self._max_hp) + "\n"
        s += "MAX_MP: " + str(self._max_mp)
        return s

    def roll_damage(self) -> int:
        return random.randint(self._atk - self._atk_swing, self._atk + self._atk_swing)

    def is_alive(self) -> bool:
        return self._hp > 0
