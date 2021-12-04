import os
import logging

# Run 'pip3 install PyObjC' to use playsound more effectively.
from playsound import playsound

LOG = logging.getLogger(__name__)


class Guitar:
    def __init__(self, model, kind):
        self.model = model
        self.kind = kind
        self.sound_dir = model + '/' + kind

    def initialize(self):
        LOG.info(f'Initializing Model: {self.model}, Type: {self.kind}')
        if not os.path.exists(self.sound_dir):
            LOG.critical(f'Directory "{self.sound_dir}" not found!')
            exit(1)

    def play(self, chord):
        LOG.info(f'Playing "{chord}"')
        audio_file = self.sound_dir + '/' + chord + ".wav"
        playsound(audio_file)

    def sequence(self, chords):
        LOG.info(f'Playing "{chords}"')
        for ch in chords.split():
            audio_file = self.sound_dir + '/' + ch + ".wav"
            playsound(audio_file)


