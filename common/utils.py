import os
import sys
import winreg

import common.constants as constants
from common.enums import VoiceEnum


def get_current_dir():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def get_resource_dir():
    return os.path.join(get_current_dir(), constants.RESOURCES_DIR)


def get_config_file():
    return os.path.join(get_current_dir(), constants.CONFIG_FILENAME)


def get_wav_file(voice: VoiceEnum):
    return os.path.join(get_resource_dir(), voice.value)


def get_steam_dir():
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, constants.STEAM_WIN_KEY, 0, winreg.KEY_READ) as registry_key:
        value, reg_type = winreg.QueryValueEx(registry_key, constants.STEAM_WIN_VALUE)
        return value.replace('/', '\\', 2)


def write_gsi_file():
    steam_dir = get_steam_dir()
    cfg_dir = os.path.join(steam_dir, constants.DOTA2_CFG_PATH)
    file_path = os.path.join(cfg_dir, constants.GSI_FILENAME)
    os.makedirs(cfg_dir, exist_ok=True)
    with open(file_path, "w") as file:
        file.write(constants.GSI_CFG_CONTENT)


def convert_seconds(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes}:{remaining_seconds:02d}"
