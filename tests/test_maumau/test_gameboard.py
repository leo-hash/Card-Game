import unittest

from src.cards import Deck
from src.maumau import PlayerMauMau, GameBoard


class TestGameboard(unittest.TestCase):

    def setUp(self):
        self.player_list = [
            PlayerMauMau("Player1"),
            PlayerMauMau("Player2"),
            PlayerMauMau("Player3"),
        ]

        self.gameboard1 = GameBoard(self.player_list, big_deck=False, double_deck=False)
        self.gameboard1.curr_player = self.player_list[0]

    def test_init(self):
        gameboard1 = GameBoard(player_list=self.player_list)
        self.assertEqual(gameboard1.player_list, self.player_list)
        self.assertEqual(gameboard1._curr_player, None)
        self.assertEqual(gameboard1._curr_player_index, None)
        self.assertEqual(gameboard1.deck.big_deck, False)
        self.assertEqual(gameboard1.deck.double_deck, False)
        self.assertNotEquals(gameboard1.deck, [])
        self.assertEqual(gameboard1.used_cards, [])

        gameboard2 = GameBoard(self.player_list, big_deck=True, double_deck=False)
        self.assertEqual(gameboard2.deck.big_deck, True)
        self.assertEqual(gameboard2.deck.double_deck, False)

        gameboard3 = GameBoard(self.player_list, big_deck=False, double_deck=True)
        self.assertEqual(gameboard3.deck.big_deck, False)
        self.assertEqual(gameboard3.deck.double_deck, True)

    def test_deal_cards(self):
        with self.assertRaises(ValueError):
            self.gameboard1.deal_cards(amount=0)

        self.gameboard1.deal_cards()
        self.assertEqual(len(self.player_list[0].hand), 1)

        self.gameboard1.deal_cards(5, self.player_list[1])
        self.assertEqual(len(self.player_list[1].hand), 5)

    def test__pick_cards(self):
        # TODO: second IndexError would occur, if every card is currently used (except last card)

        deck = Deck()
        self.gameboard1.used_cards = deck
        for i in range(32):
            try:
                self.gameboard1._pick_card(self.player_list[0])
            except IndexError:
                self.assertTrue(False, f"Deck not properly refilled after {i} cards picked")
        self.assertEqual(len(self.player_list[0].hand), 32)

    def test_last_card(self):
        raise NotImplementedError

    def test_refill_deck(self):
        raise NotImplementedError

    def test_play_card(self):
        raise NotImplementedError

    def test_move_to_next_player(self):
        raise NotImplementedError

    def test_check_player_wins(self):
        raise NotImplementedError

    def test_next_player(self):
        raise NotImplementedError

    def test__next_player_index(self):
        raise NotImplementedError

    def test_curr_player(self):
        # TODO: getter, setter, index by given player
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
