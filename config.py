import os
import json
from common import utils, constants
from typing import Union, Dict


class Setting:
    def __init__(self, dict_: Dict[str, Union[str, int, bool]]):
        self.mode: str = dict_.get('mode')
        self.stack_active: bool = dict_.get('stack_active')
        self.stack_delay: int = dict_.get('stack_delay')
        self.mid_runes_active: bool = dict_.get('mid_runes_active')
        self.mid_runes_delay: int = dict_.get('mid_runes_delay')
        self.bounty_runes_active: bool = dict_.get('bounty_runes_active')
        self.bounty_runes_delay: int = dict_.get('bounty_runes_delay')
        self.wisdom_runes_active: bool = dict_.get('wisdom_runes_active')
        self.wisdom_runes_delay: int = dict_.get('wisdom_runes_delay')
        self.lotus_active: bool = dict_.get('lotus_active')
        self.lotus_delay: int = dict_.get('lotus_delay')
        self.neutral_items_active: [bool] = dict_.get('neutral_items_active')
        self.daytime_active: bool = dict_.get('daytime_active')
        self.roshan_active: bool = dict_.get('roshan_active')
        self.first_tormentor_active: bool = dict_.get('first_tormentor_active')
        self.shard_active: bool = dict_.get('shard_active')
        self.ward_purchase_active: bool = dict_.get('ward_purchase_active')

    def to_dict(self):
        return self.__dict__


config_path = utils.get_config_file()
doc = constants.DEFAULT_CONFIG
if not os.path.exists(config_path):
    with open(config_path, "w") as fp:
        json.dump(doc, fp)
else:
    with open(config_path, 'r') as fp:
        doc = json.load(fp)
global_config = Setting(doc)


def save_config(config: Setting):
    with open(config_path, "w") as cf:
        json.dump(config.to_dict(), cf)
