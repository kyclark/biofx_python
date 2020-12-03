#!/usr/bin/env python3
"""Run-length exploding"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length exploding',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Compressed DNA text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    #for line in args.text.splitlines():
    #    print(decode(line))

    print('\n'.join(map(decode, args.text.splitlines())))


# --------------------------------------------------
def decode(text):
    """Decode DNA"""

    dna = []
    end = len(text) - 1
    for i, char in enumerate(text):
        if char.isnumeric():
            continue
        elif i == end:
            dna.append(char)
        elif text[i + 1].isnumeric():
            dna.append(char * int(text[i + 1]))
        else:
            dna.append(char)

    return ''.join(dna)


# --------------------------------------------------
def test_decode():
    """Test decode"""

    assert decode('') == ''
    assert decode('A') == 'A'
    assert decode('A2') == 'AA'
    assert decode('A2C') == 'AAC'
    assert decode('A2CG3') == 'AACGGG'
    assert decode('A2CG3T') == 'AACGGGT'


# --------------------------------------------------
if __name__ == '__main__':
    main()
