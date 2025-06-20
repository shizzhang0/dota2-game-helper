import logging

from common.enums import GameStateEnum, VoiceEnum, GameEventTypeEnum
from common.constants import GAME_MODE_QUICK
from model import GameState
from config import global_config
from gsi.speaker import voice_play

log = logging.getLogger(__name__)


class GameStateHandler:

    def __init__(self):
        self.game_start_alarmed = False
        self.daytime_alarmed = False
        self.nighttime_alarmed = False
        self.last_ward_purchase_alarmed = False
        self.last_roshan_dead_time = None
        self.past_event_keys = set()

    def handle(self, json_data):
        state = None
        try:
            state = GameState(json_data)
        except Exception as e:
            log.error(f"fail to transfer json to GameState : {e}")

        if state is None:
            return

        state_map = state.map
        state_events = state.events

        if state_map is None:
            return

        if state_map.game_state == GameStateEnum.DOTA_GAMERULES_STATE_PRE_GAME:
            if not self.game_start_alarmed:
                self.game_start_alarmed = True
                voice_play(VoiceEnum.PROLOGUE)

        if state_map.game_state == GameStateEnum.DOTA_GAMERULES_STATE_POST_GAME:
            if self.game_start_alarmed:
                self.game_start_alarmed = False
                self.daytime_alarmed = False
                self.nighttime_alarmed = False
                self.last_roshan_dead_time = None
                self.past_event_keys.clear()

        if state_map.game_state == GameStateEnum.DOTA_GAMERULES_STATE_GAME_IN_PROGRESS:
            game_time = state_map.clock_time
            is_daytime = state_map.daytime
            ward_purchase_cd = state_map.ward_purchase_cooldown

            if state_events:
                new_events = []
                if not self.past_event_keys:
                    new_events = list(state_events)
                else:
                    for event in state_events:
                        event_key = (event.event_type, event.game_time)
                        if event_key not in self.past_event_keys:
                            new_events.append(event)

                if new_events:
                    for new_event in new_events:
                        new_event_key = (new_event.event_type, new_event.game_time)
                        self.past_event_keys.add(new_event_key)
                        if new_event.event_type is GameEventTypeEnum.ROSHAN_KILLED and global_config.roshan_active:
                            self.last_roshan_dead_time = game_time

            if global_config.stack_active and game_time > 60:
                self.handle_stack(game_time)

            if global_config.mid_runes_active:
                self.handle_mid_runes(game_time)

            if global_config.bounty_runes_active:
                self.handle_bounty_runes(game_time)

            if global_config.wisdom_runes_active:
                self.handle_wisdom_runes(game_time)

            if global_config.lotus_active:
                self.handle_lotus(game_time)

            for i, neutral_item_active in enumerate(global_config.neutral_items_active):
                if neutral_item_active:
                    self.handle_neutral_items(game_time, i)

            if global_config.daytime_active and not state_map.nightstalker_night:
                self.handle_daytime(is_daytime)

            if global_config.roshan_active and self.last_roshan_dead_time is not None:
                self.handle_roshan(game_time)

            if global_config.first_tormentor_active:
                self.handle_first_tormentor(game_time)

            if global_config.shard_active:
                self.handle_shard(game_time)

            if global_config.ward_purchase_active:
                self.handle_ward_purchase(ward_purchase_cd)

    @staticmethod
    def handle_stack(game_time):
        stack_time = 60
        stack_alarm_time = stack_time - global_config.stack_delay

        if (game_time - stack_alarm_time) % stack_time == 0:
            voice_play(VoiceEnum.STACK)

    @staticmethod
    def handle_mid_runes(game_time):
        mid_runes_time = 120
        mid_runes_alarm_time = mid_runes_time - global_config.mid_runes_delay

        if (game_time - mid_runes_alarm_time) % mid_runes_time == 0:
            voice_play(VoiceEnum.MID_RUNES)

    @staticmethod
    def handle_bounty_runes(game_time):
        bounty_runes_time = 240
        bounty_runes_alarm_time = bounty_runes_time - global_config.bounty_runes_delay

        if (game_time - bounty_runes_alarm_time) % bounty_runes_time == 0:
            voice_play(VoiceEnum.BOUNTY_RUNES)

    @staticmethod
    def handle_wisdom_runes(game_time):
        wisdom_runes_time = 420
        wisdom_runes_alarm_time = wisdom_runes_time - global_config.wisdom_runes_delay

        if (game_time - wisdom_runes_alarm_time) % wisdom_runes_time == 0:
            voice_play(VoiceEnum.WISDOM_RUNES)

    @staticmethod
    def handle_lotus(game_time):
        lotus_time = 90 if global_config.mode == GAME_MODE_QUICK else 180
        lotus_alarm_time = lotus_time - global_config.lotus_delay

        if (game_time - lotus_alarm_time) % lotus_time == 0:
            voice_play(VoiceEnum.LOTUS)

    @staticmethod
    def handle_neutral_items(game_time, i):
        neutral_items_times = [210, 510, 810, 1110, 1800] if global_config.mode == GAME_MODE_QUICK else [420, 1020,
                                                                                                         1620, 2220,
                                                                                                         3600]

        if game_time == neutral_items_times[i]:
            voice_play(VoiceEnum.NEUTRAL_ITEMS)

    def handle_daytime(self, is_daytime):
        if is_daytime and not self.daytime_alarmed:
            voice_play(VoiceEnum.DAYTIME)
            self.daytime_alarmed = True
            self.nighttime_alarmed = False
        elif not is_daytime and not self.nighttime_alarmed:
            voice_play(VoiceEnum.NIGHTTIME)
            self.daytime_alarmed = False
            self.nighttime_alarmed = True

    def handle_roshan(self, game_time):
        roshan_min_time = 300 if global_config.mode == GAME_MODE_QUICK else 480
        roshan_max_time = 420 if global_config.mode == GAME_MODE_QUICK else 660

        if self.last_roshan_dead_time + roshan_min_time == game_time:
            voice_play(VoiceEnum.ROSHAN)
        elif self.last_roshan_dead_time + roshan_max_time <= game_time:
            self.last_roshan_dead_time = None

    @staticmethod
    def handle_first_tormentor(game_time):
        first_tormentor_time = 1200 if global_config.mode == GAME_MODE_QUICK else 600

        if first_tormentor_time == game_time:
            voice_play(VoiceEnum.FIRST_TORMENTOR)

    @staticmethod
    def handle_shard(game_time):
        shard_time = 600 if global_config.mode == GAME_MODE_QUICK else 900

        if shard_time == game_time:
            voice_play(VoiceEnum.SHARD)

    def handle_ward_purchase(self, ward_purchase_cd):
        if not self.last_ward_purchase_alarmed and ward_purchase_cd > 0:
            self.last_ward_purchase_alarmed = True

        if self.last_ward_purchase_alarmed and ward_purchase_cd == 0:
            self.last_ward_purchase_alarmed = False
            voice_play(VoiceEnum.WARD_PURCHASE)


game_state_handler = GameStateHandler()
