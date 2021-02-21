"""
core.py -- Core functionality
"""

from typing import List

# Flatten 2-dimensional array
def flat(digit: List[List[int]]) -> bytes:
    return bytes([i for j in digit for i in j])


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
    flat(v): int(k) for k, v in DIGITS.items()
}
