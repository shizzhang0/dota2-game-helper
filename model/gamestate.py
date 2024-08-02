from typing import Union, Dict, List
from model.map import Map
from model.player import Player
from model.provider import Provider
from model.event import Event


class GameState:
    def __init__(self, dict_: Dict[str, Union[str, Dict]]):
        self.provider: Provider = Provider(dict_.get('provider')) if dict_.get('provider') else None
        self.map: Map = Map(dict_.get('map')) if dict_.get('map') else None
        self.player: Player = Player(dict_.get('player')) if dict_.get('player') else None
        self.events: List[Event] = [Event(e) for e in dict_.get('events')] if dict_.get('events') else []
