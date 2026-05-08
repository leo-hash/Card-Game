from src.cards import Card, Rank
from src.maumau import GameBoard
from src.maumau import PlayerMauMau
import random

from src.maumau.agent import Agent
from src.maumau.game_config import GameConfig, GameboardConfig, PlayerConfig


class GameEngine:

    def __init__(self, config: GameConfig):
        self.players, self.agents = self._create_players(config.players)
        self.gameboard = self._create_board(config.board, self.players)
        self._setup_game()


    @staticmethod
    def _create_board(board_config: GameboardConfig, player_list: list[PlayerMauMau]) -> GameBoard:
        return GameBoard(
            player_list=player_list,
            big_deck=board_config.big_deck,
            double_deck=board_config.double_deck
        )

    @staticmethod
    def _create_players(player_config: list[PlayerConfig]) -> tuple[list[PlayerMauMau], dict[str, Agent]]:
        player_list = []
        agent_list = {}
        for p in player_config:
            player_list.append(PlayerMauMau(name=p.name))
            agent_list.update({p.name: p.agent})
        return player_list, agent_list

    def _setup_game(self, start_player_index: int=None, card_count: int = 6):
        if start_player_index is None:
            self.gameboard.curr_player = random.choice(self.players)
        else:
            if start_player_index < 0 or start_player_index >= len(self.players):
                raise ValueError("Invalid start_player index")
            else:
                self.gameboard.curr_player = self.players[start_player_index]

        for player in self.players:
            self.gameboard.deal_cards(amount=card_count, player=player)

        self.gameboard.setup_last_card()

    def _apply_card_effect(self, card: Card):
        # 7: draw two, without multiple 7 in a row
        if card.rank is Rank.SEVEN:
            print(f"Player {self.gameboard.next_player().name} has to draw 2 cards")
            self.gameboard.deal_cards(2, self.gameboard.next_player())

        # 8: suspend next player
        if card.rank is Rank.EIGHT:
            print(f"Player {self.gameboard.next_player().name} is suspended for this round")
            self.gameboard.move_to_next_player()

        # Jack: choose a color
        if card.rank is Rank.JACK:
            # TODO: implement jack
            pass

    def play_turn(self):
        cur_agent = self.agents[self.gameboard.curr_player.name]
        card_to_play = cur_agent.choose_card(self.gameboard)

        # if card_to_play == null, then draw a card
        if card_to_play is None:
            print(f"Player {self.gameboard.curr_player.name} has to draw a card")
            self.gameboard.deal_cards(1, self.gameboard.curr_player)
        else:
            # if card_to_play legal move, play
            top_card = self.gameboard.show_last_card()
            if (card_to_play.suit == top_card.suit or
                    card_to_play.rank == top_card.rank):
                print(f"Player {self.gameboard.curr_player.name} played {card_to_play}")
                self.gameboard.play_card(card_to_play)
                self._apply_card_effect(card_to_play)
                if self.gameboard.check_player_wins():
                    self.end_game()
                self.gameboard.move_to_next_player()

            else:
                # illegal move
                print(f"Player {self.gameboard.curr_player.name} made illegal move, try again")
                self.play_turn()


    def end_game(self):
        exit()


