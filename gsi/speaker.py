import logging
from threading import Thread
from common.enums import VoiceEnum
from common import utils
import winsound

log = logging.getLogger(__name__)


class SpeakerTask(Thread):
    def __init__(self, voice: VoiceEnum):
        super().__init__()
        self.voice = voice

    def run(self):
        try:
            filename = utils.get_wav_file(self.voice)
            winsound.PlaySound(filename, winsound.SND_FILENAME or winsound.SND_ASYNC or winsound.SND_NODEFAULT)
        except Exception as e:
            log.error(f"fail to play voice file : {e}")


def voice_play(voice: VoiceEnum):
    task = SpeakerTask(voice)
    task.start()
