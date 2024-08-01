from typing import Union, Dict, List
from model.map import Map
from model.player import Player
from model.provider import Provider
from model.event import Event


class GameState:
    def __init__(self, dict_: Dict[str, Union[str, Dict]]):
        self.provider: Provider = Provider(dict_.get('provider'))
        self.map: Map = Map(dict_.get('map'))
        self.player: Player = Player(dict_.get('player'))
        self.events: List[Event] = [Event(e) for e in dict_.get('events')]
