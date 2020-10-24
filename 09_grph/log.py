#!/usr/bin/env python3

import sys

print('This is STDOUT.')
print('This is also STDOUT.', file=sys.stdout)
print('This is STDERR.', file=sys.stderr)
