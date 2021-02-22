import itertools

from typing import Dict, List

from .core import ALTERNATIVES, ENCODING_MAP


def permutate(digit_str: str) -> List[str]:
    for idx, d in enumerate(digit_str):
        if d in ALTERNATIVES:
            # copy character sequence into list of strings
            alt = [x for x in digit_str] 
            # replace string at index `idx` with a list of possible alternatives
            alt[idx] = ALTERNATIVES[d]
            yield from alternatives(alt)


def alternatives(alt: List[List[str]]):
    for x in itertools.product(*alt):
        yield "".join(x)


def matches_per_digit(d: bytes) -> Dict[str, int]:
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


def best_guess(d: bytes) -> List[str]:
    """
    Return a list of best matching digits based on the given digit `d`.
    """
    items = matches_per_digit(d).items()
    match = [k for k, v in items if v == 9]  # full match
    if len(match):
        return match
    return [k for k, v in items if v == 8]  # match with 1 char difference
