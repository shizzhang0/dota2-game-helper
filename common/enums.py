from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def values(cls):
        return [member.value for member in cls]


class VoiceEnum(BaseEnum):
    PROLOGUE = 'prologue.wav'
    STACK = 'alarm_stack.wav'
    MID_RUNES = 'alarm_mid_runes.wav'
    BOUNTY_RUNES = 'alarm_bounty_runes.wav'
    WISDOM_RUNES = 'alarm_wisdom_runes.wav'
    LOTUS = 'alarm_lotus.wav'
    NEUTRAL_ITEMS = 'alarm_neutral_items.wav'
    DAYTIME = 'alarm_daytime.wav'
    NIGHTTIME = 'alarm_night_time.wav'
    ROSHAN = 'alarm_roshan.wav'
    FIRST_TORMENTOR = 'alarm_first_tormentor.wav'
    SHARD = 'alarm_shard.wav'


class GameStateEnum(BaseEnum):
    DOTA_GAMERULES_STATE_INIT = 'DOTA_GAMERULES_STATE_INIT'
    DOTA_GAMERULES_STATE_WAIT_FOR_PLAYERS_TO_LOAD = 'DOTA_GAMERULES_STATE_WAIT_FOR_PLAYERS_TO_LOAD'
    DOTA_GAMERULES_STATE_CUSTOM_GAME_SETUP = 'DOTA_GAMERULES_STATE_CUSTOM_GAME_SETUP'
    DOTA_GAMERULES_STATE_HERO_SELECTION = 'DOTA_GAMERULES_STATE_HERO_SELECTION'
    DOTA_GAMERULES_STATE_STRATEGY_TIME = 'DOTA_GAMERULES_STATE_STRATEGY_TIME'
    DOTA_GAMERULES_STATE_TEAM_SHOWCASE = 'DOTA_GAMERULES_STATE_TEAM_SHOWCASE'
    DOTA_GAMERULES_STATE_PRE_GAME = 'DOTA_GAMERULES_STATE_PRE_GAME'
    DOTA_GAMERULES_STATE_GAME_IN_PROGRESS = 'DOTA_GAMERULES_STATE_GAME_IN_PROGRESS'
    DOTA_GAMERULES_STATE_POST_GAME = 'DOTA_GAMERULES_STATE_POST_GAME'
    DOTA_GAMERULES_STATE_DISCONNECT = 'DOTA_GAMERULES_STATE_DISCONNECT'


class GameEventTypeEnum(BaseEnum):
    BOUNTY_RUNE_PICKUP = 'bounty_rune_pickup'
    AEGIS_PICKED_UP = 'aegis_picked_up'
    ROSHAN_KILLED = 'roshan_killed'
    TIP = 'tip'
