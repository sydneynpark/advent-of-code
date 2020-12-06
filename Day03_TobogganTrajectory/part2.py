from slope import Slope


def aim_and_traverse(x, y, slope):
    slope.aim(x, y)
    tree_crashes = slope.traverse()
    print('You hit {} trees.'.format(tree_crashes))
    return tree_crashes


if __name__ == '__main__':
    print('Reading map')
    toboggan_slope = Slope.read_map('./resources/toboggan_slope.txt')

    crashes = [
        aim_and_traverse(x, y, toboggan_slope)
        for (x, y)
        in [(1,1), (3,1), (5,1), (7,1), (1,2)]
    ]

    crash_product = 1
    for crash_count in crashes:
        crash_product *= crash_count

    print('Your crash product is {}'.format(crash_product))