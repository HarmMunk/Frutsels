import unittest
import deck_of_cards


class TestDeckOfCardsMethods(unittest.TestCase):
    def test_nr_of_cards_in_deck(self):
        self.assertEqual(len(deck_of_cards.Deck()), 52, "Not 52 cards in deck")

    def test_suits_in_deck(self):
        d = deck_of_cards.Deck()
        suits = {s: 0 for s in 'spades hearts clubs diamonds'.split()}
        for c in d:
            suits[c.suit] += 1
        for s in suits:
            self.assertEqual(suits[s], 13, "Not 13 cards of " + s)

    def test_ranks_in_deck(self):
        d = deck_of_cards.Deck()
        ranks = {r: 0 for r in [str(n) for n in range(2, 11)] + list('JKQA')}
        for c in d:
            ranks[c.rank] += 1
        for r in ranks:
            self.assertEqual(ranks[r], 4, "Not 4 cards of " + r)

    def test_dealing_cards(self):
        d = deck_of_cards.Deck()
        dealt_cards = []
        while d:
            c = d.deal()
            self.assertFalse(c in d, str(c) + " is dealt but still in the deck")
            dealt_cards += deck_of_cards.Card(c.rank, c.suit)
        self.assertEqual(len(dealt_cards), 52, "deck is empty but less than 52 cards dealt")


if __name__ == '__main__':
    unittest.main()
