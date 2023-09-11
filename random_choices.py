import random
import importlib
from typing import cast

class Failed:
    def __init__(self):
        __str__ = "fail"


class Success:
    def __init__(self):
        __str__ = "success"

def main():
    match random.choice(["heads", "tails"]):
        case random.choice(
            []
        ):