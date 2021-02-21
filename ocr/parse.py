"""
parse.py -- Parse OCR file containing account entries
"""

import argparse

from typing import Generator, Iterable, List

from .core import ENCODING_MAP, matrix_to_bytes, to_ord


def checksum(account_no: str) -> int:
    if len(account_no) > 0:
        return int(account_no[0]) * len(account_no) + checksum(account_no[1:])
    return 0


def verify_checksum(account_no: str) -> bool:
    return checksum(account_no) % 11 == 0


def lines_to_digits(lines: List[str]) -> Generator:
    for x in range(9):
        sl = slice(3 * x, 3 * x + 3)
        d = [
            to_ord(lines[0][sl]),
            to_ord(lines[1][sl]),
            to_ord(lines[2][sl]),
        ]
        yield matrix_to_bytes(d)


def digits_to_account_no(digits: Iterable[bytes]) -> str:
    return "".join(
        ENCODING_MAP.get(d, "?") for d in digits
    )


def parse_file_to_lines(fp) -> Generator:
    while True:
        try:
            yield [l.strip("\n").ljust(27) for l in [
                next(fp),
                next(fp),
                next(fp),
            ]]
        except StopIteration:
            break
        else:
            # read and dismiss newline
            next(fp)


def parse(args: argparse.Namespace) -> None:
    """
    CLI entry point for parsing OCR file into account numbers.
    """
    for lines in parse_file_to_lines(args.infile):
        digits_gen = lines_to_digits(lines)
        account_no = digits_to_account_no(digits_gen)
        print(account_no, file=args.outfile)


def check(args: argparse.Namespace) -> None:
    """
    CLI entry point for adding ERR/ILL after account number if
    checksum is invalid.
    """
    for lines in parse_file_to_lines(args.infile):
        digits_gen = lines_to_digits(lines)
        account_no = digits_to_account_no(digits_gen)
        info = ""
        if "?" in account_no:
            info = "ILL"
        elif not verify_checksum(account_no):
            info = "ERR"
        print(account_no, info, file=args.outfile)
