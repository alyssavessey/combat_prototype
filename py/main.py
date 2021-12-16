#!/usr/bin/env python3

import random
from player import Player

def main() -> None:
    random.seed()
    p: Player = Player()
    print(p)

main()
