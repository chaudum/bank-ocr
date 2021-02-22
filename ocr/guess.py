import itertools
from typing import Dict, Generator, List

from .core import _HEX_DIGITS, ENCODING_MAP, hexlify


def alternatives(alt: List[List[str]]) -> Generator[str, None, None]:
    for x in itertools.product(*alt):
        yield "".join(x)


def matches_per_digit(d: str) -> Dict[str, int]:
    """
    A digit is a sequence of 9 (3x3) characters.
    This function calculates for the given digit `d` the sum of matching
    characters for each digit (0-9).
    """
    diff = {}
    for k, v in ENCODING_MAP.items():
        assert len(k) == len(d), "character sequences must be of same length"
        res = [1 if k[i] == d[i] else 0 for i in range(len(k))]
        diff[v] = sum(res)
    return diff


def best_guess(d: str, yield_exact_match: bool = True) -> List[str]:
    """
    A digit is a sequence of 9 (3x3) characters.
    Return a list of best matching digits based on the given digit `d`.
    """
    items = matches_per_digit(d).items()
    match = [k for k, v in items if v == 9]  # full match
    if len(match) and yield_exact_match:
        return match
    return [k for k, v in items if v == 8]  # match with 1 char difference


ALTERNATIVES = {
    hexlify(idx): best_guess(item, yield_exact_match=False) for idx, item in enumerate(_HEX_DIGITS)
}

def permutate(digit_str: str) -> Generator[str, None, None]:
    """
    Yield all permutations of a digit string by replacing a single digit of a
    digit string with a best match (add or remove single character).
    """
    for idx, d in enumerate(digit_str):
        if d in ALTERNATIVES:
            # copy character sequence into list of strings
            alt = [[x] for x in digit_str] 
            # replace string at index `idx` with a list of possible alternatives
            alt[idx] = ALTERNATIVES[d]
            yield from alternatives(alt)
