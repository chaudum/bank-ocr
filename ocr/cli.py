"""
ocr.py -- Main entry point for CLI
"""

import argparse
import sys

from .generate import main as g
from .parse import main as p
from .parse import add_checksum


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(title="subcommands")

    generate = commands.add_parser("generate")
    generate.add_argument("--entries", "-n", type=int, default=500)
    generate.set_defaults(func=g)

    parse = commands.add_parser("parse")
    parse.add_argument("--infile", type=argparse.FileType("r"), default=sys.stdin)
    parse.set_defaults(func=p)

    parse = commands.add_parser("check")
    parse.add_argument("--infile", type=argparse.FileType("r"), default=sys.stdin)
    parse.set_defaults(func=add_checksum)

    parser.add_argument("--outfile", type=argparse.FileType("w"), default=sys.stdout)
    parser.set_defaults(func=None)
    return parser


def main() -> None:
    parser = get_parser()
    args = parser.parse_args()
    if not args.func:
        parser.print_help()
        sys.exit(2)
    args.func(args)


if __name__ == "__main__":
    main()
