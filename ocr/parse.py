"""
parse.py -- Parse OCR file containing account entries
"""

import argparse

from typing import Iterable, List

from .core import ENCODING_MAP, flat


def to_ord(s: str) -> List[int]:
    return [ord(ch) for ch in s]


def checksum(account_no: str) -> int:
    if len(account_no) > 0:
        return int(account_no[0]) * len(account_no) + checksum(account_no[1:])
    return 0


def verify_checksum(account_no: str) -> bool:
    return checksum(account_no) % 11 == 0


def lines_to_digits(lines: List[str]) -> str:
    digits = []
    for x in range(9):
        sl = slice(3 * x, 3 * x + 3)
        d = [
            to_ord(lines[0][sl]),
            to_ord(lines[1][sl]),
            to_ord(lines[2][sl]),
        ]
        digits.append(d)
    return [flat(d) for d in digits]


def main(args: argparse.Namespace) -> None:
    """
    CLI entry point for parsing OCR file into account numbers.
    """
    while True:
        try:
            lines = [l.strip("\n").ljust(27) for l in [
                next(args.infile),
                next(args.infile),
                next(args.infile),
            ]]
        except StopIteration:
            break
        else:

            print("".join(str(ENCODING_MAP.get(d, "?")) for d in lines_to_digits(lines)), file=args.outfile)

        # read and dismiss newline
        next(args.infile)


def add_checksum(args: argparse.Namespace):
    """
    CLI entry point for adding ERR after account number if checksum
    is invalid.
    """
    for line in args.infile:
        account_no = line.strip("\n")
        info = ""
        if "?" in account_no:
            info = "ILL"
        elif not verify_checksum(account_no):
            info = "ERR"
        print(account_no, info, file=args.outfile)
