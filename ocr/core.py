"""
core.py -- Core functionality
"""

from typing import Iterable, List


def hexlify(i: int) -> str:
    """
    Convert integer into a HEX string representation

    >>> hexlify(1)
    1
    >>> hexlify(10)
    A
    >>> hexlify(255)
    FF
    """

    return str.upper("{:0x}".format(i))


def splice(s: str, l: int) -> List[str]:
    """
    Convert character sequence `s` into list of strings with length `l`.

    >>> splice("123456", 3)
    ["123", "456"]

    >>> splice("abcdef", 2)
    ["ab", "cd", "ef"]

    >>> splice("123", 5)
    ["123  "]
    """

    if len(s) > l:
        return [s[0:l]] + splice(s[l:], l)
    else:
        return [s[0:].ljust(l)]


_HEX_DIGITS = [
    (
        " _ "
        "| |"
        "|_|"
    ),
    (
        "   "
        "  |"
        "  |"
    ),
    (
        " _ "
        " _|"
        "|_ "
    ),
    (
        " _ "
        " _|"
        " _|"
    ),
    (
        "   "
        "|_|"
        "  |"
    ),
    (
        " _ "
        "|_ "
        " _|"
    ),
    (
        " _ "
        "|_ "
        "|_|"
    ),
    (
        " _ "
        "  |"
        "  |"
    ),
    (
        " _ "
        "|_|"
        "|_|"
    ),
    (
        " _ "
        "|_|"
        " _|"
    ),
    (
        " _ "
        "|_|"
        "| |"
    ),
    (
        " _ "
        "|_\\"
        "|_/"
    ),
    (
        " _ "
        "|  "
        "|_ "
    ),
    (
        " _ "
        "| \\"
        "|_/"
    ),
    (
        " _ "
        "|_ "
        "|_ "
    ),
    (
        " _ "
        "|_ "
        "|  "
    ),
]

HEX_DIGITS = {hexlify(idx): [i for i in splice(x, 3)] for idx, x in enumerate(_HEX_DIGITS)}

ENCODING_MAP = {
    item: hexlify(idx) for idx, item in enumerate(_HEX_DIGITS)
}
