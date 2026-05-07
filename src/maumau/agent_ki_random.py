# from typing import override

from src.cards import Card
from src.maumau import GameBoard
from src.maumau.agent import Agent


class AgentKiRandom(Agent):

    # @override
    def choose_card(self, gameboard: GameBoard) -> Card:
        pass