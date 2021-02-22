import argparse
import itertools
from typing import Generator, Iterable, List, Tuple

from .checksum import verify_checksum
from .core import ENCODING_MAP
from .guess import alternatives, best_guess, permutate


def parse_lines_to_digits(lines: List[str], n: int = 3, l: int = 9) -> Generator[str, None, None]:
    for line in lines:
        assert len(line) == n * l, f"lines must contain of {n * l} characters"

    for x in range(l):
        sl = slice(n * x, n * x + n)
        yield "".join([line[sl] for line in lines])


def digits_to_account_no(digits_gen: Generator[str, None, None], check=False, autofix=False) -> Tuple[str, str]:
    digits = [d for d in digits_gen]
    digit_str = "".join(ENCODING_MAP.get(d, "?") for d in digits)

    info = ""
    if check:
        # Perform validity checks
        if "?" in digit_str:
            if autofix:
                # Perform best guess
                alt = [a for a in alternatives([best_guess(d) for d in digits]) if verify_checksum(a)]
                if len(alt) == 0:
                    info = "ERR"
                elif len(alt) == 1:
                    digit_str = alt[0]
                elif len(alt) > 1:
                    info = "AMB"
            else:
                info = "ILL"
        elif not verify_checksum(digit_str):
            if autofix:
                # Perform best guess
                alt = [a for a in permutate(digit_str) if verify_checksum(a)]
                if len(alt) == 0:
                    info = "ERR"
                elif len(alt) == 1:
                    digit_str = alt[0]
                elif len(alt) > 1:
                    info = "AMB"
            else:
                info = "ERR"

    return digit_str, info


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
        digits_gen = parse_lines_to_digits(lines)
        digit_str, info = digits_to_account_no(
            digits_gen, check=args.check, autofix=args.fixit,
        )
        print(digit_str, info, file=args.outfile)
