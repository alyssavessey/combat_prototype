# A basic healing spell

import random
import spell
from creature import Creature
from player import Player

class Heal(spell.Spell):
    _MIN_HEAL = 20
    _MAX_HEAL = 30

    def __init__(self):
        super(self, 4, 'Heal')

    def cast(self, caster: Creature, target: Creature) -> None:
        gain: int = random.randint(Heal._MIN_HEAL, Heal._MAX_HEAL)
        if isinstance(caster, Player):
            caster.change_hp(gain)

