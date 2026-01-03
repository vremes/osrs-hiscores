# OSRS Hiscores

Simple OSRS Hiscores client for Python.

---

## Installation

```bash
pip install osrs-hiscores
```


## Usage

```py
    from osrs_hiscores.client import HiscoresClient

    rsn = "Lynx Titan"

    client = HiscoresClient()

    stats = client.get_player_stats(rsn)

    print(f"Player {stats.rsn} has agility level of {stats.skills.agility.level}, {stats.skills.agility.experience} experience and rank {stats.skills.agility.rank}.")
    # Player Lynx Titan has agility level of 99, 200000000 experience and rank 24.

    # You can also loop all skills if you want to!
    for skill in stats.skills:
        print(f"Player {stats.rsn} has {skill.name} level of {skill.level}, {skill.experience} and rank {skill.rank}")

    # Player Lynx Titan has Total level of 2278, 4600000000 and rank 83066
    # Player Lynx Titan has Attack level of 99, 200000000 and rank 15
    # Player Lynx Titan has Defence level of 99, 200000000 and rank 28
    # Player Lynx Titan has Strength level of 99, 200000000 and rank 18
    # Player Lynx Titan has Hitpoints level of 99, 200000000 and rank 7
    # Player Lynx Titan has Ranged level of 99, 200000000 and rank 8
    # Player Lynx Titan has Prayer level of 99, 200000000 and rank 11
    # Player Lynx Titan has Magic level of 99, 200000000 and rank 29
    # Player Lynx Titan has Cooking level of 99, 200000000 and rank 150
    # Player Lynx Titan has Woodcutting level of 99, 200000000 and rank 15
    # Player Lynx Titan has Fletching level of 99, 200000000 and rank 12
    # Player Lynx Titan has Fishing level of 99, 200000000 and rank 9
    # Player Lynx Titan has Firemaking level of 99, 200000000 and rank 48
    # Player Lynx Titan has Crafting level of 99, 200000000 and rank 4
    # Player Lynx Titan has Smithing level of 99, 200000000 and rank 3
    # Player Lynx Titan has Mining level of 99, 200000000 and rank 23
    # Player Lynx Titan has Herblore level of 99, 200000000 and rank 5
    # Player Lynx Titan has Agility level of 99, 200000000 and rank 24
    # Player Lynx Titan has Thieving level of 99, 200000000 and rank 12
    # Player Lynx Titan has Slayer level of 99, 200000000 and rank 2
    # Player Lynx Titan has Farming level of 99, 200000000 and rank 19
    # Player Lynx Titan has Runecrafting level of 99, 200000000 and rank 6
    # Player Lynx Titan has Hunter level of 99, 200000000 and rank 4
    # Player Lynx Titan has Construction level of 99, 200000000 and rank 4
    # Player Lynx Titan has Sailing level of 1, 0 and rank -1
```
