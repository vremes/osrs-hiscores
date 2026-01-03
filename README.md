# OSRS Hiscores

Simple OSRS Hiscores client for Python.

---

## Installation

```bash
pip install osrs-hiscores-client
```


## Usage

```py
from osrs_hiscores.client import HiscoresClient

rsn = "Lynx Titan"

client = HiscoresClient()

stats = client.get_player_stats(rsn)

print(f"Player {stats.rsn} has agility (ID: {stats.skills.agility.id}) level of {stats.skills.agility.level}, {stats.skills.agility.experience} experience and rank {stats.skills.agility.rank}.")
# Player Lynx Titan has agility (ID: 17) level of 99, 200000000 experience and rank 24.

# You can also loop all skills if you want to!
for skill in stats.skills:
    print(f"Player {stats.rsn} has {skill.name} (ID: {skill.id}) level of {skill.level}, {skill.experience} experience and rank {skill.rank}")

# Player Lynx Titan has Overall (ID: 0) level of 2278, 4600000000 experience and rank 83146
# Player Lynx Titan has Attack (ID: 1) level of 99, 200000000 experience and rank 15
# Player Lynx Titan has Defence (ID: 2) level of 99, 200000000 experience and rank 28
# Player Lynx Titan has Strength (ID: 3) level of 99, 200000000 experience and rank 18
# Player Lynx Titan has Hitpoints (ID: 4) level of 99, 200000000 experience and rank 7
# ...

# Each object can be turn into dictionary if need.
print(stats.skills.cooking.to_dict())
# {'name': 'Cooking', 'rank': 150, 'level': 99, 'experience': 200000000}
```
