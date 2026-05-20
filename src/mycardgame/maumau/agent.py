from abc import ABC, abstractmethod

from mycardgame.cards import Card
from mycardgame.maumau import GameBoard


class Agent(ABC):

    @abstractmethod
    def choose_card(self, gameboard: GameBoard) -> Card:
        pass