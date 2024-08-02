RESOURCES_DIR = 'resources'

CONFIG_FILENAME = 'config.json'

DEFAULT_CONFIG = {
    'mode': 'normal',
    'stack_active': True,
    'stack_delay': 15,
    'mid_runes_active': True,
    'mid_runes_delay': 10,
    'bounty_runes_active': True,
    'bounty_runes_delay': 15,
    'wisdom_runes_active': True,
    'wisdom_runes_delay': 15,
    'lotus_active': True,
    'lotus_delay': 15,
    'neutral_items_active': True,
    'daytime_active': True,
    'roshan_active': True,
    'first_tormentor_active': True,
    'shard_active': True
}

GSI_FILENAME = 'gamestate_integration_d2gh.cfg'

GSI_CFG_CONTENT = '''"Dota2 Game Helper Integration Configuration"
{
    "uri"       "http://localhost:3000"
    "timeout"   "5.0"
    "buffer"    "0.1"
    "throttle"  "0.1"
    "heartbeat" "30.0"
    "data"
    {
        "provider"  "1"
        "map"       "1"
        "player"    "1"
        "event"     "1"
        "hero"      "1"
        "abilities" "1"
        "items"     "1"
    }
}'''

GAME_MODE_NORMAL = 'normal'
GAME_MODE_QUICK = 'quick'

STEAM_WIN_KEY = r'Software\Valve\Steam'
STEAM_WIN_VALUE = 'SteamPath'
DOTA2_CFG_PATH = 'steamapps\\common\\dota 2 beta\\game\\dota\\cfg\\gamestate_integration'
