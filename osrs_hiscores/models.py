from dataclasses import dataclass, fields, asdict
from typing import Iterator
from .enums import Skill as SkillEnum


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

    id: int
    name: str
    rank: int
    level: int
    experience: int

    @classmethod
    def from_json(cls, json: dict) -> "Skill":
        """
        Creates Skill from JSON data.

        :param json: JSON data as dictionary.
        :type json: dict
        :return: Skill data class which contains skill data.
        :rtype: Skill
        """
        id: int = json["id"]
        name: str = json["name"]
        rank: int = json["rank"]
        level: int = json["level"]
        experience: int = json["xp"]

        return cls(id, name, rank, level, experience)


@dataclass(frozen=True)
class SkillsCollection(Base):
    """
    Represents a collection of skills.
    """

    overall: Skill
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
    runecraft: Skill
    hunter: Skill
    construction: Skill
    sailing: Skill

    def __iter__(self) -> Iterator[Skill]:
        for field in fields(self):
            yield getattr(self, field.name)

    @classmethod
    def from_json(cls, json: dict) -> "SkillsCollection":
        """
        Creates SkillsCollection from JSON data.

        :param json: JSON data as dictionary.
        :type json: dict
        :return: SkillsCollection data class which contains all skills and their data.
        :rtype: SkillsCollection
        """
        skills_json = json["skills"]

        skills_dict: dict[str, Skill] = {}

        for skill_enum in SkillEnum:
            skill_json: dict = skills_json[skill_enum.value]
            skill_name: str = skill_json["name"]
            skills_dict[skill_name.lower()] = Skill.from_json(skill_json)

        return SkillsCollection(**skills_dict)


@dataclass(frozen=True)
class PlayerStats(Base):
    rsn: str
    skills: SkillsCollection

    @classmethod
    def from_json(cls, json: dict) -> "PlayerStats":
        """
        Creates PlayerStats from JSON data.

        :param json: JSON data as dictionary.
        :type json: dict
        :return: PlayerStats data class which contains skills.
        :rtype: PlayerStats
        """
        skills: SkillsCollection = SkillsCollection.from_json(json)
        return cls(json["name"], skills)
