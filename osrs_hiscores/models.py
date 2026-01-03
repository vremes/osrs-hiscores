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

    name: str
    rank: int
    level: int
    experience: int


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
        Parses the JSON from hiscores API into SkillsCollection data class.

        :param json: JSON from Hiscores API.
        :type json: dict
        :return: SkillsCollection data class which contains all skills and their data.
        :rtype: SkillsCollection
        """
        json_skills = json["skills"]

        skills_dict: dict[str, Skill] = {}

        for skill_enum in SkillEnum:
            skill: dict = json_skills[skill_enum.value]

            skill_name: str = skill["name"]
            skill_rank: int = skill["rank"]
            skill_level: int = skill["level"]
            skill_experience: int = skill["xp"]

            skills_dict[skill_name.lower()] = Skill(
                skill_name, skill_rank, skill_level, skill_experience
            )

        return SkillsCollection(**skills_dict)


@dataclass(frozen=True)
class PlayerStats(Base):
    rsn: str
    skills: SkillsCollection

    @classmethod
    def from_json(cls, json: dict) -> "PlayerStats":
        skills: SkillsCollection = SkillsCollection.from_json(json)
        return cls(json["name"], skills)
