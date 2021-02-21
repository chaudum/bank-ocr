"""
checksum.py
"""

def checksum(digit_str: str) -> int:
    if len(digit_str) > 0:
        return int(digit_str[0]) * len(digit_str) + checksum(digit_str[1:])
    return 0


def verify_checksum(digit_str: str) -> bool:
    return checksum(digit_str) % 11 == 0
