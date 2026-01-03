from requests import Session
from .models import PlayerStats


class HiscoresClient:
    """
    Client for OSRS Hiscores API.
    """

    def __init__(self, session: Session | None = None):
        """
        Initializes the client.

        :param session: Optional requests Session, usually not needed.
        :type session: Session | None
        """
        self.session = session or Session()

    def get_player_stats(self, rsn: str) -> PlayerStats:
        """
        Returns player's stats from hiscores API as PlayerStats dataclass.

        :param rsn: Player name (e.g. 'Zezima')
        :type rsn: str
        :return: PlayerStats dataclass which includes player's RSN and skills.
        :rtype: PlayerStats
        """
        url: str = (
            f"https://services.runescape.com/m=hiscore_oldschool/index_lite.json?player={rsn}"
        )
        response = self.session.get(url)
        response.raise_for_status()
        response_json = response.json()
        return PlayerStats.from_json(response_json)
