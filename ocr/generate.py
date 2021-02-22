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

from typing import List

from .core import ENCODING_MAP, HEX_DIGITS


def digits_to_lines(chars: str) -> List[str]:
    lines = [[], [], []]
    for ch in chars:
        digit = HEX_DIGITS[ch]
        for idx, line in enumerate(lines):
            lines[idx] += digit[idx]
    return lines


def main(args: argparse.Namespace):
    chars = list(ENCODING_MAP.values())
    for n in range(args.entries):
        x = "".join(random.choice(chars) for _ in range(9))
        for line in digits_to_lines(x):
            print("".join(line), file=args.outfile)
        print("", file=args.outfile)
