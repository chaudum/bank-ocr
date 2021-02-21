"""
core.py -- Core functionality
"""

from typing import Iterable, List

from .types import Matrix


def matrix_to_bytes(digit: Matrix) -> bytes:
    """
    Convert 2d matrix (3x3) into bytes array.
    """
    return bytes([i for j in digit for i in j])


def to_ord(s: Iterable) -> List[int]:
    return [ord(ch) for ch in s]


def bytes_to_matrix(digit: bytes) -> Matrix:
    """
    Convert bytes array into 2d matrix (3x3).
    """
    return [
        to_ord(digit[0:3]),
        to_ord(digit[3:6]),
        to_ord(digit[6:9]),
    ]


# ordinals for the 3 different characters
# S(pace)
# H(orizontal)
# V(ertical)
S, H, V = ord(" "), ord("_"), ord("|")

# Map of digit (0..9) to 3x3 matrix
# Each digit is represented by 3 ordinal numbers in 3 lines
DIGITS = {
    "0": [[S, H, S], [V, S, V], [V, H, V]],
    "1": [[S, S, S], [S, S, V], [S, S, V]],
    "2": [[S, H, S], [S, H, V], [V, H, S]],
    "3": [[S, H, S], [S, H, V], [S, H, V]],
    "4": [[S, S, S], [V, H, V], [S, S, V]],
    "5": [[S, H, S], [V, H, S], [S, H, V]],
    "6": [[S, H, S], [V, H, S], [V, H, V]],
    "7": [[S, H, S], [S, S, V], [S, S, V]],
    "8": [[S, H, S], [V, H, V], [V, H, V]],
    "9": [[S, H, S], [V, H, V], [S, H, V]],
}

ENCODING_MAP = {
    matrix_to_bytes(v): k for k, v in DIGITS.items()
}

ALTERNATIVES = {
    "0": ["8"],
    "1": ["7"],
    "5": ["9", "6"],
    "6": ["8"],
    "9": ["8"],
}
