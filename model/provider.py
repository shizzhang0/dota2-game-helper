from typing import Union, Dict


class Provider:
    def __init__(self, dict_: Dict[str, Union[str, int]]):
        self.name: str = dict_.get('name')
        self.appid: int = dict_.get('appid')
        self.version: int = dict_.get('version')
        self.timestamp: int = dict_.get('timestamp')
