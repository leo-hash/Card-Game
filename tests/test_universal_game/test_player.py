import unittest

from src.mycardgame.cards import Deck
from src.mycardgame.universal_game import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.deck.create_new_deck()
        self.deck.shuffle()


    def test_init(self):
        name1 = "player1"
        name2 = "player2"
        player1 = Player(name1)
        player2 = Player(name2, self.deck.cards[:16])

        self.assertEqual(player1.name, name1)
        self.assertEqual(player1.hand, [])

        self.assertEqual(player2.name, name2)
        self.assertEqual(player2.hand, self.deck.cards[:16])

    def test_play_card(self):
        player = Player("player", self.deck.cards[:2])

        self.assertEqual(player.play_card(self.deck.cards[0]), self.deck.cards[0])
        self.assertEqual(player.play_card(self.deck.cards[1]), self.deck.cards[1])

        with self.assertRaises(ValueError):
            player.play_card(self.deck.cards[0])

        with self.assertRaises(ValueError):
            player.play_card(self.deck.cards[2])


    def test_receive_card(self):
        player = Player("player")

        with self.assertRaises(ValueError):
            player.receive_card()

        with self.assertRaises(ValueError):
            player.receive_card(card=self.deck.cards[0], card_list=self.deck.cards[:3])

        player.receive_card(card=self.deck.cards[1])
        self.assertEqual(player.hand.pop(), self.deck.cards[1])

        player.receive_card(card_list=self.deck.cards[:4])
        self.assertEqual(player.hand, self.deck.cards[:4])

if __name__ == '__main__':
    unittest.main()
