from slope import Slope




if __name__ == '__main__':
    print('Reading map')
    toboggan_slope = Slope.read_map('./resources/toboggan_slope.txt')
    print('Aiming...')
    toboggan_slope.aim(3, 1)
    print('And we\'re off!')
    tree_crashes = toboggan_slope.traverse()

    print('You hit {} trees.'.format(tree_crashes))