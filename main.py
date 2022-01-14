from typing import TypeVar

T = TypeVar("T", bytes, str)


def some_func(test_str: T):
    cmdline: str | int = test_str
