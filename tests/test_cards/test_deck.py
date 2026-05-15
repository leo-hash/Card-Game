import unittest
from src.cards.deck import Deck, Card, Rank, Suit

class TestDeck(unittest.TestCase):
    def test_constructor(self):
        deck1 = Deck(False, True)
        deck2 = Deck(True, False)

        self.assertEqual(deck1.big_deck, False)
        self.assertEqual(deck1.double_deck, True)

        self.assertEqual(deck2.big_deck, True)
        self.assertEqual(deck2.double_deck, False)

    def test_create_new_deck_check_amount(self):
        deck1 = Deck(False, False)
        deck2 = Deck(True, False)
        deck3 = Deck(False, True)
        deck4 = Deck(True, True)

        deck1.create_new_deck()
        self.assertEqual(len(deck1.cards), 32)

        deck2.create_new_deck()
        self.assertEqual(len(deck2.cards), 52)

        deck3.create_new_deck()
        self.assertEqual(len(deck3.cards), 64)

        deck4.create_new_deck()
        self.assertEqual(len(deck4.cards), 104)

    def test_create_new_deck_check_cards(self):
        deck1 = Deck(True, True)
        deck1.create_new_deck()

        for suit in Suit:
            for rank in Rank:
                self.assertEqual(Card(suit, rank) in deck1.cards, True,
                                 f"Deck does not contain {suit} {rank} ")


    def test_add_card_errors(self):
        deck1 = Deck(False, False)
        deck2 = Deck(True, False)

        card1 = Card(Suit.HEARTS, Rank.SEVEN)
        card2 = Card(Suit.CLUBS, Rank.EIGHT)
        card3 = Card(Suit.SPADES, Rank.SIX)

        card_list = [card1, card2]

        with self.assertRaises(ValueError):
            deck1.add_card(None, None)

        with self.assertRaises(ValueError):
            deck1.add_card(card1, card_list)

        with self.assertRaises(ValueError):
            deck1.add_card(card3)

        deck2.add_card(card3)


    def test_add_card_content(self):
        deck1 = Deck(False, False)
        deck2 = Deck(True, False)

        card1 = Card(Suit.HEARTS, Rank.SEVEN)
        card2 = Card(Suit.CLUBS, Rank.EIGHT)
        card3 = Card(Suit.SPADES, Rank.SIX)

        card_list = [card1, card2]

        deck1.add_card(card1)
        self.assertEqual(deck1.cards[0], card1)
        deck1.cards.clear()

        deck1.add_card(card_list=card_list)
        self.assertEqual(deck1.cards, card_list)
        deck1.cards.clear()

        deck2.add_card(card3)
        self.assertEqual(deck2.cards[0], card3)
        deck2.cards.clear()


    def test_shuffle(self):
        raise NotImplementedError

    def test_draw_card(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
