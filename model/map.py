from typing import Union, Dict
from common.enums import GameStateEnum


class Map:
    def __init__(self, dict_: Dict[str, Union[str, int, bool]]):
        self.name: str = dict_.get('name')
        self.match_id: str = dict_.get("matchid")
        self.game_time: int = dict_.get("game_time")
        self.clock_time: int = dict_.get("clock_time")
        self.daytime: bool = dict_.get("daytime")
        self.nightstalker_night: bool = dict_.get("nightstalker_night")
        self.radiant_score: int = dict_.get("radiant_score")
        self.dire_score: int = dict_.get("dire_score")
        self.game_state: GameStateEnum = GameStateEnum(dict_.get("game_state")) if dict_.get(
            "game_state") in GameStateEnum.values() else None
        self.paused: bool = dict_.get('paused')
        self.win_team: str = dict_.get('win_team')
        self.custom_game_name: str = dict_.get('customgamename')
        self.ward_purchase_cooldown: int = dict_.get('ward_purchase_cooldown')
