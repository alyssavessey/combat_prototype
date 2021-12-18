import creature
import random

class Player(creature.Creature):
    _MIN_ATK_GAIN: int = 2
    _MAX_ATK_GAIN: int = 3
    _MIN_DEF_GAIN: int = 2
    _MAX_DEF_GAIN: int = 3
    _MIN_HP_GAIN: int = 5
    _MAX_HP_GAIN: int = 9
    _MIN_MP_GAIN: int = 2
    _MAX_MP_GAIN: int = 4

    _level: int = 0
    _max_hp: int = 0
    _max_mp: int = 0

    def __init__(self, level: int) -> None:
        self._level = level
        atk = 0
        deff = 0
        for i in range(1, self._level + 1):
            atk += random.randint(self._MIN_ATK_GAIN, self._MAX_ATK_GAIN)
            deff += random.randint(self._MIN_DEF_GAIN, self._MAX_DEF_GAIN)
            self._max_hp += random.randint(self._MIN_HP_GAIN, self._MAX_HP_GAIN)
            self._max_mp += random.randint(self._MIN_MP_GAIN, self._MAX_HP_GAIN)
        super().__init__(
            atk = atk,
            deff = deff,
            atk_swing = 2,
            hp = self._max_hp,
            mp = 0)

    def __str__(self) -> str:
        s: str = ""
        s += "ATK: " + str(self._atk) + "\n"
        s += "DEF: " + str(self._def) + "\n"
        s += "MAX_HP: " + str(self._max_hp) + "\n"
        s += "MAX_MP: " + str(self._max_mp)
        return s
