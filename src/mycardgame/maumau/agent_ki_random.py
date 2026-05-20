from mycardgame.cards import Card
from mycardgame.maumau import GameBoard
from mycardgame.maumau.agent import Agent

import random
from typing_extensions import override


class AgentKiRandom(Agent):

    @override
    def choose_card(self, gameboard: GameBoard) -> Card | None:
        my_player = gameboard.curr_player
        last_card = gameboard.last_played_card

        poss_cards = list(filter(
            lambda x: x.suit is last_card.suit or
                      x.rank is last_card.rank,
            my_player.hand))

        # change empty list to None -> draw a card
        if len(poss_cards) <= 0: return None
        return random.choice(poss_cards)
