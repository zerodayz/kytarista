from guitar import Guitar

import config


def main():
    config.setup_logging()
    guitar = Guitar('slg200s', 'acoustic')
    guitar.initialize()
    ch = guitar.chord('c')
    seq1 = guitar.sequence('c d a c d a c d a c a')
    seq2 = guitar.sequence('a a a a')
    sound = guitar.pick('c d e f g a b c1')
    # combined = guitar.overlay(seq1, sound, gain_during_overlay=-8)
    faster = guitar.speed_change(sound)
    guitar.play(sound)


if __name__ == '__main__':
    main()
