import unittest
from src.cards.deck import Deck, Card, Rank, Suit

class MyTestCase(unittest.TestCase):
    def test_constructor(self):
        deck1 = Deck(False, True)
        deck2 = Deck(True, False)

        self.assertEqual(deck1.big_deck, False)
        self.assertEqual(deck1.double_deck, True)

        self.assertEqual(deck2.big_deck, True)
        self.assertEqual(deck2.double_deck, False)

    def test_create_new_deck(self):
        raise NotImplementedError

    def test_add_card(self):
        raise NotImplementedError

    def test_shuffle(self):
        raise NotImplementedError

    def test_draw_card(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
