from guitar import Guitar


def main():
    guitar = Guitar('slg200s', 'acoustic')
    guitar.initialize()
    guitar.play('c')
    guitar.sequence('c d e f#')


if __name__ == '__main__':
    main()
