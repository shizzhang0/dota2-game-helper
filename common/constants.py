RESOURCES_DIR = 'resources'

ICON_FILENAME = 'd2gh.ico'

CONFIG_FILENAME = 'config.json'

DEFAULT_CONFIG = {
    'mode': 'normal',
    'stack_active': False,
    'stack_delay': 18,
    'mid_runes_active': False,
    'mid_runes_delay': 6,
    'bounty_runes_active': False,
    'bounty_runes_delay': 13,
    'wisdom_runes_active': True,
    'wisdom_runes_delay': 15,
    'lotus_active': False,
    'lotus_delay': 8,
    'neutral_items_active': [False, False, False, False, True],
    'daytime_active': False,
    'roshan_active': True,
    'first_tormentor_active': True,
    'shard_active': True,
    'ward_purchase_active': False,
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
        "events"    "1"
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
