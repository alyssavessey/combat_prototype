# Abstract base class for all magic

import math
import random
from creature import Creature

class Spell():
    _FIZZLE_CHANCE: float = 0.15
    _FIZZLE_WEIGHT: float = 0.25

    _cost: int = 0
    _fizzle_cost: int = 0
    _name: str = ""

    def __init__(self, cost, name):
        self._cost = cost
        self._fizzle_cost = Spell._calculate_fizzle_cost(self._cost)
        self._name = name

    def __str__(self) -> str:
        return "{}: {} MP".format(self._name, self._cost)

    def cast(self, caster: Creature, target: Creature) -> None:
        pass

    def pay(self, caster: Creature) -> None:
        cost: int = self._cost
        if random.random() < Spell._FIZZLE_CHANCE:
            cost += self._fizzle_cost
        caster._mp -= cost
        if caster._mp < 0:
            caster._hp += caster._mp
            caster._mp = 0

    @staticmethod
    def _calculate_fizzle_cost(_cost: int) -> int:
        exact_cost: float = Spell._FIZZLE_WEIGHT * float(_cost)
        cost: int = int(math.floor(exact_cost))
        if cost <= 0:
            cost = 1
        return cost
