from kytarista import Guitar

import config


def main():
    config.setup_logging()
    guitar = Guitar('slg200s', 'acoustic')
    guitar.initialize()
    strums = guitar.sequence('a c d e') 
    guitar.play(strums)


if __name__ == '__main__':
    main()
