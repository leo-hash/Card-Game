import unittest

from src.cards import Deck, Card
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
        self.assertNotEqual(gameboard1.deck, [])
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

    def test_last_card_and_play_card(self):
        # maybe a bit lazy but setup_last_card, last_played_card and play_card are oneliners
        # and player.play_card is already tested in test_player
        self.gameboard1.deal_cards(5)

        self.gameboard1.setup_last_card()
        self.assertTrue(isinstance(self.gameboard1.last_played_card, Card))

        for i in range(5):
            last_card = self.player_list[0].hand[0]
            self.gameboard1.play_card(self.player_list[0].hand[0])
            self.assertEqual(self.gameboard1.last_played_card, last_card)


    def test_refill_deck(self):
        with self.assertRaises(ValueError):
            self.gameboard1.refill_deck()

        self.gameboard1.deal_cards(20)
        for i in range(20):
            self.gameboard1.play_card(self.player_list[0].hand[0])
        self.gameboard1.refill_deck()

        self.assertEqual(len(self.gameboard1.used_cards), 1)
        self.assertEqual(len(self.gameboard1.deck.cards), 31)

    def test_move_to_next_player(self):
        for i in range(6):
            next_player = self.gameboard1.next_player
            self.gameboard1.move_to_next_player()
            self.assertEqual(next_player, self.gameboard1.curr_player)

    def test_remove_current_player(self):
        self.gameboard1.remove_current_player()
        self.assertEqual(self.gameboard1.player_list, self.player_list[:2])

        self.gameboard1.move_to_next_player()
        self.gameboard1.remove_current_player()
        self.assertEqual(self.gameboard1.player_list, self.player_list[:1])


    def test_check_player_wins(self):
        self.assertTrue(self.gameboard1.check_player_wins())

        self.gameboard1.deal_cards(1)
        self.assertFalse(self.gameboard1.check_player_wins())

    def test_check_game_over(self):
        self.assertFalse(self.gameboard1.check_game_over())

        self.gameboard1.remove_current_player()
        self.gameboard1.move_to_next_player()
        self.gameboard1.remove_current_player()
        self.gameboard1.move_to_next_player()

        self.assertTrue(self.gameboard1.check_game_over())

    def test_curr_player(self):
        self.gameboard1.curr_player = self.player_list[0]
        self.assertEqual(self.gameboard1.curr_player, self.player_list[0])

        self.gameboard1.curr_player = self.player_list[1]
        self.assertEqual(self.gameboard1.curr_player, self.player_list[1])

        self.gameboard1.curr_player = self.player_list[2]
        self.assertEqual(self.gameboard1.curr_player, self.player_list[2])

if __name__ == '__main__':
    unittest.main()
