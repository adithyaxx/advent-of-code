import numpy as np
import collections


def get_rating(bits, is_oxygen=True):
    loops = bits.shape[1]

    for i in range(loops):
        if bits.shape[0] == 1:
            break

        counts = collections.Counter(bits[:, i])
        if is_oxygen:
            keep = '0' if counts['0'] > counts['1'] else '1'
        else:
            keep = '1' if counts['0'] > counts['1'] else '0'

        bits = bits[bits[:, i] == keep]

    return int(''.join(bits.flatten()), 2)


if __name__ == '__main__':
    with open('input.txt') as f:
        inp = np.array([list(x) for x in f.read().splitlines()])
        inp = np.array(inp)

    oxygen_rating = get_rating(inp, True)
    c02_rating = get_rating(inp, False)

    print(oxygen_rating * c02_rating)
