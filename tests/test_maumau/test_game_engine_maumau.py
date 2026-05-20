import unittest

from mycardgame.cards import Card
from mycardgame.maumau import PlayerMauMau
from mycardgame.maumau.agent_ki_random import AgentKiRandom
from mycardgame.maumau.game_config import GameConfig, GameboardConfig, PlayerConfig
from mycardgame.maumau import GameEngine


class TestGameEngine(unittest.TestCase):
    def setUp(self):
        self.game_config = GameConfig(
            board=GameboardConfig(big_deck=False, double_deck=False),
            players=[
                PlayerConfig(name='KI_1', agent=AgentKiRandom()),
                PlayerConfig(name='KI_2', agent=AgentKiRandom()),
                PlayerConfig(name='KI_3', agent=AgentKiRandom())
            ]
        )
        self.engine1 = GameEngine(self.game_config)


    def test_init(self):
        self.assertEqual(self.engine1.gameboard.deck.big_deck, self.game_config.board.big_deck)
        self.assertEqual(self.engine1.gameboard.deck.double_deck, self.game_config.board.double_deck)

        for i in range(len(self.game_config.players)):
            self.assertEqual(self.engine1.gameboard.player_list[i].name, self.game_config.players[i].name)
            self.assertEqual(self.engine1.players[i].name, self.game_config.players[i].name)
            self.assertEqual(self.engine1.agents.get(self.game_config.players[i].name), self.game_config.players[i].agent)

    def test_setup_game(self):
        self.engine1.setup_game()
        self.assertIsInstance(self.engine1.gameboard.curr_player, PlayerMauMau)
        self.assertIsInstance(self.engine1.gameboard.last_played_card, Card)
        for players in self.engine1.players:
            self.assertEqual(len(players.hand), 6)

        self.engine1 = GameEngine(self.game_config)
        self.engine1.setup_game(start_player_index=1, card_count=10)
        self.assertTrue(self.engine1.gameboard.curr_player, self.engine1.players[1])
        self.assertIsInstance(self.engine1.gameboard.last_played_card, Card)
        for players in self.engine1.players:
            self.assertEqual(len(players.hand), 10)

        self.engine1 = GameEngine(self.game_config)
        with self.assertRaises(ValueError):
            self.engine1.setup_game(start_player_index=-1)
        with self.assertRaises(ValueError):
            self.engine1.setup_game(start_player_index=3)

    def play_turn(self):
        # draw, legal move, player_wins, game over
        # card effects: 7, 8
        pass



if __name__ == '__main__':
    unittest.main()
