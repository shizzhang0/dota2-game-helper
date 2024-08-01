from typing import Dict, Union


class Player:
    def __init__(self, dict_: Dict[str, Union[str, int, Dict[str, int]]]):
        self.steam_id: str = dict_.get('steamid')
        self.account_id: str = dict_.get('accountid')
        self.name: str = dict_.get('name')
        self.activity: str = dict_.get('activity')
        self.kills: int = dict_.get('kills')
        self.deaths: int = dict_.get('deaths')
        self.assists: int = dict_.get('assists')
        self.last_hits: int = dict_.get('last_hits')
        self.denies: int = dict_.get('denies')
        self.kill_streak: int = dict_.get('kill_streak')
        self.commands_issued: int = dict_.get('commands_issued')
        self.kill_list: Dict[str, int] = dict_.get('kill_list')
        self.team_name: str = dict_.get('team_name')
        self.player_slot: int = dict_.get('player_slot')
        self.team_slot: int = dict_.get('team_slot')
        self.gold: int = dict_.get('gold')
        self.gold_reliable: int = dict_.get('gold_reliable')
        self.gold_unreliable: int = dict_.get('gold_unreliable')
        self.gold_from_hero_kills: int = dict_.get('gold_from_hero_kills')
        self.gold_from_creep_kills: int = dict_.get('gold_from_creep_kills')
        self.gold_from_income: int = dict_.get('gold_from_income')
        self.gold_from_shared: int = dict_.get('gold_from_shared')
        self.gold_per_minute: int = dict_.get('gpm')
        self.experience_per_minute: int = dict_.get('xpm')
