import argparse
import itertools

from typing import Generator, Iterable, List

from .checksum import verify_checksum
from .core import ALTERNATIVES, ENCODING_MAP, matrix_to_bytes, to_ord
from .guess import alternatives, best_guess, permutate


def lines_to_digits(lines: List[str]) -> Generator:
    for x in range(9):
        sl = slice(3 * x, 3 * x + 3)
        d = [
            to_ord(lines[0][sl]),
            to_ord(lines[1][sl]),
            to_ord(lines[2][sl]),
        ]
        yield matrix_to_bytes(d)


def digits_to_account_no(digits: Iterable[bytes], check=False, autofix=False) -> str:
    tmp = [d for d in digits]
    account_no = "".join(ENCODING_MAP.get(d, "?") for d in tmp)

    info = ""
    if check:
        # Perform validity checks
        if "?" in account_no:
            if autofix:
                # Perform best guess
                alt = [a for a in alternatives([best_guess(d) for d in tmp]) if verify_checksum(a)]
                if len(alt) == 0:
                    info = "ERR"
                elif len(alt) == 1:
                    account_no = alt[0]
                elif len(alt) > 1:
                    info = "AMB"
            else:
                info = "ILL"
        elif not verify_checksum(account_no):
            if autofix:
                # Perform best guess
                alt = [a for a in permutate(account_no) if verify_checksum(a)]
                if len(alt) == 0:
                    info = "ERR"
                elif len(alt) == 1:
                    account_no = alt[0]
                elif len(alt) > 1:
                    info = "AMB"
            else:
                info = "ERR"

    return account_no, info


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


def main(args: argparse.Namespace) -> None:
    """
    CLI entry point for parsing OCR file into account numbers.
    """
    for lines in parse_file_to_lines(args.infile):
        digits_gen = lines_to_digits(lines)
        account_no, info = digits_to_account_no(
            digits_gen, check=args.check, autofix=args.fixit,
        )
        print(account_no, info, file=args.outfile)
