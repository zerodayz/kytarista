from kytarista import Guitar

import config


def main():
    config.setup_logging()
    guitar = Guitar('slg200s', 'acoustic')
    guitar.initialize()
    seq1 = guitar.sequence('a a a a')
    seq2 = guitar.sequence('d d d d')
    g = guitar.pick('high-e-g# high-e-open')
    c = guitar.pick('high-e-b high-e-open')
    a = guitar.pick('high-e-a high-e-open')
    c = guitar.pick('high-e-c high-e-open')

    # combined = guitar.overlay(seq1, sound, gain_during_overlay=-8)
    faster = guitar.speed_change(seq1 + seq2)
    guitar.play(seq1)


if __name__ == '__main__':
    main()
