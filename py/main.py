#!/usr/bin/env python3

import random
from player import Player
from monster import Monster

def query_player(msg: str) -> int:
    print(msg, end='')
    return int(input())

def combat(player: Player) -> None:
    monster: Monster = Monster()
    print("A monster approaches!")
    while combat_continues(player, monster):
        player_turn(player, monster)
        if not combat_continues(player, monster):
            break
        monster_turn(player, monster)

def combat_continues(player: Player, monster: Monster) -> bool:
    if player._hp <= 0:
        print("You died!")
        return False
    elif monster._hp <= 0:
        print("You slew the monster!")
        return False
    return True

def player_turn(player: Player, monster: Monster) -> None:
    print("You have {}/{} HP.".format(player._hp, player._max_hp))
    print("1) Fight")
    print("2) Magic (unimplemented)")
    print("3) Item (unimplemented)")
    print("4) Flee (unimplemented)")
    while True:
        command: int = query_player("Command? ")
        if command == 1:
            damage: int = player.roll_damage(monster._def)
            print("Dealt {} damage!".format(damage))
            monster._hp -= damage
            break
        else:
            print("Invalid command!")

def monster_turn(player: Player, monster: Monster) -> None:
    damage: int = monster.roll_damage(player._def)
    print("The monster struck you for {} damage!".format(damage))
    player._hp -= damage

def main() -> None:
    random.seed()
    level: int = query_player("Enter player level: ")
    player: Player = Player(level)
    combat(player)

main()
