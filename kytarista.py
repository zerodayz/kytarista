from guitar import Guitar
import config


def main():
    config.setup_logging()
    guitar = Guitar('slg200s', 'acoustic')
    guitar.initialize()
    seq1 = guitar.sequence('a a a a')
    seq2 = guitar.sequence('d d d d')
    sound = guitar.pick('c d e f g a b c1')
    combined = guitar.overlay(seq1, sound, gain_during_overlay=-8)
    guitar.play(combined)


if __name__ == '__main__':
    main()
