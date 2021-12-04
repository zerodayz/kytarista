import os
# Run 'pip3 install PyObjC' to use playsound more effectively.
from playsound import playsound


class Guitar:
    def __init__(self, model, kind):
        self.model = model
        self.kind = kind
        self.sound_dir = model + '/' + kind

    def initialize(self):
        print(f'Initializing model {self.model}, type {self.kind}')
        if os.path.exists(self.sound_dir):
            print(f'OK')
        else:
            print(f'FATAL')
            print(f'Directory "{self.sound_dir}" not found!')
            exit(1)

    def play(self, chord):
        print(f'Playing {chord}')
        audio_file = self.sound_dir + '/' + chord + ".wav"
        playsound(audio_file)

    def sequence(self, chords):
        print(f'Playing {chords}')
        for ch in chords.split():
            audio_file = self.sound_dir + '/' + ch + ".wav"
            playsound(audio_file)


