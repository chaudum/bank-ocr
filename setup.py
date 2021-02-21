from setuptools import setup

setup(
    name="bank-ocr",
    author="Christian Haudum",
    packages=["ocr"],
    entry_points={
        "console_scripts": [
            "bank-ocr = ocr.cli:main",
        ],
    },
)
