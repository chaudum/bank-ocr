# Bank OCR

## Disclaimer

> This repository contains a solution for a kata as part of an interview process.

## Installation

To install this program, create a virtualenv and install the package locally into the environment:


```
python3 -m venv env
source env/bin/activate
(env) python -m pip install -Ue .
```

## Usage

To see all available commands invoke the installed CLI application with the `--help` argument:

```
(env) bank-ocr --help
```

To generate a `testfile.ocr`, run the `generate` command:

```
(env) bank-ocr generate -n 500 > testfile.ocr
```

### User Story 1

```
(env) cat testfile.ocr | bank-ocr parse
```

### User Story 2 + 3

Use the `--check` argument to report validty of the parsed account numbers.

```
(env) cat testfile.ocr | bank-ocr parse --check
```

### User Story 4

Use the `--fixit` argument to replace invalid or ambiguous digits of invalid account numbers with a best guess.

```
(env) cat testfile.ocr | bank-ocr parse --check --fixit
```
