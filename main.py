from kytarista import Guitar

import config


def main():
    config.setup_logging()
    guitar = Guitar('slg200s', 'acoustic')
    guitar.initialize()
    strums = guitar.sequence('a a a a')
    strums2 = guitar.sequence('d d d d')
    g = guitar.pick('high-e-g# high-e-open')
    c = guitar.pick('high-e-b high-e-open')
    a = guitar.pick('high-e-a high-e-open')
    c2 = guitar.pick('high-e-c high-e-open')
    combo1 = (g + c) * 2
    combo2 = (a + c2) * 2
    guitar.play(strums + strums2)
    # sound = guitar.speed_change(combo1 + combo2, playback_speed=4)
    # combined = guitar.overlay(seq1, sound, gain_during_overlay=-8)


if __name__ == '__main__':
    main()
