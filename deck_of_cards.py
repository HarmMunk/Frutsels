from collections import namedtuple
import random
from typing import List

Card = namedtuple('Card', ['rank', 'suit'])


class Deck:
    ranks: List[str] = [str(n) for n in range(2, 11)] + list('JKQA')
    suits: List[str] = 'spades hearts clubs diamonds'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
        self._crd = None

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, item) -> Card:
        return self._cards[item]

    def deal(self):
        self._crd = random.choice(self._cards)
        self._cards.remove(self._crd)
        return self._crd

    def new_deck(self):
        self.__init__()


if __name__ == "__main__":
    d = Deck()

    print(d[:])

    for i in range(0, 52):
        print(d.deal())
        print(d[:])
