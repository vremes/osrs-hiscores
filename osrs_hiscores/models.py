from dataclasses import dataclass, fields, asdict
from typing import Iterator


class Base:
    """
    Base class for models.
    """

    def to_dict(self):
        """
        Returns the dataclass as a dictionary.
        """
        return asdict(self)


@dataclass(frozen=True)
class Skill(Base):
    """
    Represents player's skill.
    """

    name: str
    rank: int
    level: int
    experience: int


@dataclass(frozen=True)
class SkillsCollection(Base):
    """
    Represents a collection of skills.
    """

    total: Skill
    attack: Skill
    defence: Skill
    strength: Skill
    hitpoints: Skill
    ranged: Skill
    prayer: Skill
    magic: Skill
    cooking: Skill
    woodcutting: Skill
    fletching: Skill
    fishing: Skill
    firemaking: Skill
    crafting: Skill
    smithing: Skill
    mining: Skill
    herblore: Skill
    agility: Skill
    thieving: Skill
    slayer: Skill
    farming: Skill
    runecrafting: Skill
    hunter: Skill
    construction: Skill
    sailing: Skill

    def __iter__(self) -> Iterator[Skill]:
        for field in fields(self):
            yield getattr(self, field.name)


@dataclass(frozen=True)
class PlayerStats(Base):
    rsn: str
    skills: SkillsCollection
