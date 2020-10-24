#!/usr/bin/env python3
""" Run the test suite on all solution*.py """

import argparse
import os
import re
import shutil
import sys
import subprocess
from subprocess import getstatusoutput
from functools import partial
from typing import NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    program: str
    quiet: bool


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Run the test suite on all solution*.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('program', metavar='prg', help='Program to test')

    parser.add_argument('-q', '--quiet', action='store_true', help='Be quiet')

    args = parser.parse_args()

    return Args(args.program, args.quiet)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    cwd = os.getcwd()
    solutions = list(
        filter(partial(re.match, r'solution.*\.py'), os.listdir(cwd)))

    for solution in sorted(solutions):
        print(f'==> {solution} <==')
        shutil.copyfile(solution, os.path.join(cwd, args.program))
        subprocess.run(['chmod', '+x', args.program], check=True)
        rv, out = getstatusoutput('make test')
        if rv != 0:
            sys.exit(out)

        if not args.quiet:
            print(out)

    print('Done.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
