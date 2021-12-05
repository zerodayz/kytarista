import os
import logging

from pydub import AudioSegment
from pydub import effects
from pydub.playback import play

import constants as consts

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

    def chord(self, chord, end=consts.DEFAULT_END):
        audio_file = self.sound_dir + '/' + chord + ".wav"
        sound = AudioSegment.from_file(audio_file, format="wav")
        return sound[:end]

    def sequence(self, chords, end=consts.DEFAULT_END):
        combined = AudioSegment.empty()

        for ch in chords.split():
            audio_file = self.sound_dir + '/' + ch + ".wav"
            sound = AudioSegment.from_file(audio_file, format="wav")
            combined += sound[:end]
        return combined

    def speed_change(self, audio, **args):
        output = effects.speedup(audio, **args)
        return output

    def pick(self, chords, end=consts.DEFAULT_END):
        combined = AudioSegment.empty()

        for ch in chords.split():
            audio_file = self.sound_dir + '/pick_' + ch + ".wav"
            sound = AudioSegment.from_file(audio_file, format="wav")
            combined += sound[:end]
        return combined

    def play(self, audio):
        audio_out = effects.strip_silence(audio, silence_len=1,
                                          silence_thresh=-50, padding=0)
        play(audio_out)

    def sleep(self, ms):
        silence = AudioSegment.silent(duration=ms)
        return silence

    def overlay(self, first, second, **kwargs):
        combined = first.overlay(second, **kwargs)
        return combined
