"""
generate.py -- Utility to generate test file

Usage:

$ python generate.py -h 
usage: generate.py [-h] [--outfile OUTFILE] [--entries ENTRIES]

optional arguments:
  -h, --help            show this help message and exit
  --outfile OUTFILE
  --entries ENTRIES, -n ENTRIES

"""

import argparse
import random
import sys

from .core import DIGITS
from .types import Matrix


def digits_to_lines(value: int) -> str:
    lines = [[], [], []]
    for i in str(value):
        digit = DIGITS[i]
        for idx, line in enumerate(lines):
            lines[idx] += digit[idx]
    return lines


def print_lines(lines: Matrix, file=None) -> None:
    for line in lines:
        print("".join(chr(ch) for ch in line), file=file)


def main(args: argparse.Namespace):
    for n in range(args.entries):
        x = random.randint(111111111, 999999999)
        print_lines(digits_to_lines(x), file=args.outfile)
        print()
