from enums import Skill as SkillEnum
from models import Skill, PlayerStats, SkillsCollection


def parse_player_stats(rsn: str, response_text: str) -> PlayerStats:
    """
    Parses the response from hiscores API into PlayerStats dataclass.

    :param rsn: Runescape player name.
    :type rsn: str
    :param response_text: The raw response text from hiscores API.
    :type response_text: str
    """
    skill_lines = response_text.splitlines()

    rank_key, level_key, experience_key = [0, 1, 2]

    skills_dict: dict[str, Skill] = {}

    for skill in SkillEnum:
        skill_line_raw: str = skill_lines[skill.value]
        skill_line_values: list = skill_line_raw.split(",")

        skill_rank: int = get_skill_line_value(rank_key, skill_line_values)
        skill_level: int = get_skill_line_value(level_key, skill_line_values)
        skill_experience: int = get_skill_line_value(experience_key, skill_line_values)

        skills_dict[skill.name.lower()] = Skill(
            skill.name.title(), skill_rank, skill_level, skill_experience
        )

    return PlayerStats(rsn, SkillsCollection(**skills_dict))


def get_skill_line_value(
    key: int, skill_line_values: list[str], default: int = 0
) -> int:
    """
    Returns specified key from the skill line values, e.g. rank for the skill.

    :param key: Key for the value, for example 0 is the key for rank.
    :type key: int
    :param skill_line_values: Skill line values from the hiscores API.
    :type skill_line_values: list[str]
    :param default: The default value to return if key does not exist in skill_line_values.
    :type default: int
    :return: Returns the value for key or default value.
    :rtype: int
    """
    try:
        return int(skill_line_values[key])
    except (IndexError, ValueError):
        return default
