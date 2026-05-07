from abc import ABC, abstractmethod

from src.cards import Card
from src.maumau import GameBoard


class Agent(ABC):

    @abstractmethod
    def choose_card(self, gameboard: GameBoard) -> Card:
        pass