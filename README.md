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

```
(env) cat testfile.ocr | bank-ocr parse | bank-ocr check
```
