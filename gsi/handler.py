import logging

from common.enums import GameStateEnum
from model import GameState
from config import global_config

log = logging.getLogger(__name__)


def handle_game_state(json_data):
    state = None
    try:
        state = GameState(json_data)
    except Exception as e:
        log.error(e)

    if state is None:
        return

    state_map = state.map
    if state_map is not None and state_map.game_state == GameStateEnum.DOTA_GAMERULES_STATE_GAME_IN_PROGRESS:
        game_time = state_map.clock_time
        is_daytime = state_map.daytime
