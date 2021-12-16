#!/usr/bin/env python3

import random

class Player():
    _LEVEL: int = 10
    _MIN_ATK_GAIN: int = 2
    _MAX_ATK_GAIN: int = 3
    _MIN_DEF_GAIN: int = 2
    _MAX_DEF_GAIN: int = 3
    _MIN_HP_GAIN: int = 5
    _MAX_HP_GAIN: int = 9
    _MIN_MP_GAIN: int = 2
    _MAX_MP_GAIN: int = 4

    _atk = 0
    _def = 0
    _max_hp = 0
    _max_mp = 0

    def __init__(self) -> None:
        for i in range(1, self._LEVEL + 1):
            self._atk += random.randint(self._MIN_ATK_GAIN, self._MAX_ATK_GAIN)
            self._def += random.randint(self._MIN_DEF_GAIN, self._MAX_DEF_GAIN)
            self._max_hp += random.randint(self._MIN_HP_GAIN, self._MAX_HP_GAIN)
            self._max_mp += random.randint(self._MIN_MP_GAIN, self._MAX_HP_GAIN)

    def __str__(self) -> str:
        s: str = ""
        s += "ATK: " + str(self._atk) + "\n"
        s += "DEF: " + str(self._def) + "\n"
        s += "MAX_HP: " + str(self._max_hp) + "\n"
        s += "MAX_MP: " + str(self._max_mp)
        return s

def main() -> None:
    random.seed()
    p: Player = Player()
    print(p)

main()
