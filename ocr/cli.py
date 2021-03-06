"""
ocr.py -- Main entry point for CLI
"""

import argparse
import sys

from .generate import main as generate
from .parse import main as parse


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(title="subcommands")

    cmd_generate = commands.add_parser("generate")
    cmd_generate.add_argument("--entries", "-n", type=int, default=500)
    cmd_generate.set_defaults(func=generate)

    cmd_parse = commands.add_parser("parse")
    cmd_parse.add_argument("--infile", type=argparse.FileType("r"), default=sys.stdin)
    cmd_parse.add_argument("--check", action="store_true", default=False)
    cmd_parse.add_argument("--fixit", action="store_true", default=False)
    cmd_parse.set_defaults(func=parse)

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
