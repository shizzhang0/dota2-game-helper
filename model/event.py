from typing import Union, Dict
from common.enums import GameEventTypeEnum


class Event:
    def __init__(self, dict_: Dict[str, Union[str, int]]):
        self.game_time: int = dict_.get('game_time')
        self.event_type: GameEventTypeEnum = GameEventTypeEnum(dict_.get('event_type')) if dict_.get(
            'event_type') in GameEventTypeEnum.values() else None
