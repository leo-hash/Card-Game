import unittest
from src.cards import Card, Rank, Suit


class MyTestCase(unittest.TestCase):
    def test_constructor_errors(self):
        with self.assertRaises(TypeError):
            card1 = Card(rank=Rank.SEVEN, suit='Hearts')

        with self.assertRaises(TypeError):
            card2 = Card(rank=7, suit=Suit.HEARTS)

        with self.assertRaises(ValueError):
            card3 = Card(rank=Rank.SIX, suit=Suit.HEARTS, big_deck=False)

    def test_constructor_happy_path(self):
        card1 = Card(rank=Rank.KING, suit=Suit.HEARTS)
        card2 = Card(rank=Rank.ACE, suit=Suit.DIAMONDS)
        card3 = Card(rank=Rank.NINE, suit=Suit.SPADES, big_deck=True)
        card4 = Card(rank=Rank.TWO, suit=Suit.CLUBS, big_deck=True)

        self.assertEqual(card1.rank, Rank.KING)
        self.assertEqual(card1.suit, Suit.HEARTS)
        self.assertEqual(card1.big_deck, False)

        self.assertEqual(card2.rank, Rank.ACE)
        self.assertEqual(card2.suit, Suit.DIAMONDS)
        self.assertEqual(card2.big_deck, False)

        self.assertEqual(card3.rank, Rank.NINE)
        self.assertEqual(card3.suit, Suit.SPADES)
        self.assertEqual(card3.big_deck, True)

        self.assertEqual(card4.rank, Rank.TWO)
        self.assertEqual(card4.suit, Suit.CLUBS)
        self.assertEqual(card4.big_deck, True)


if __name__ == '__main__':
    unittest.main()
