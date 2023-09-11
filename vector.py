import math


class Vector:

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __repr__(self):
        return f'Vevtor({self._x!r}, {self._y!r})'

    def __abs__(self):
        return math.hypot(self._x, self._y)

    def __bytes__(self):
        return bool(self._x) or bool(self._y)