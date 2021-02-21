import itertools

from typing import Dict, List

from .core import ALTERNATIVES, ENCODING_MAP


def permutate(account_no: str) -> List[str]:
    for idx, d in enumerate(account_no):
        if d in ALTERNATIVES:
            alt = [x for x in account_no]
            alt[idx] = ALTERNATIVES[d]
            yield from alternatives(alt)


def alternatives(alt: List[List[str]]):
    for x in itertools.product(*alt):
        yield "".join(x)


def calculate_diff(d: bytes) -> Dict[str, int]:
    diff = {}
    for k, v in ENCODING_MAP.items():
        assert len(k) == len(d), "sequence must be of same length"
        res = []
        for i in range(len(k)):
            res.append(1 if k[i] == d[i] else 0)
        diff[v] = sum(res)
    return diff


def best_guess(d: bytes) -> List[str]:
    items = calculate_diff(d).items()
    match = [k for k, v in items if v == 9]
    if len(match):
        return match
    return [k for k, v in items if v == 8]
