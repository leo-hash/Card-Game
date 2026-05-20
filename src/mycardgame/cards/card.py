from mycardgame.cards.suit import Suit
from mycardgame.cards.rank import Rank

from dataclasses import dataclass

@dataclass
class Card:
    suit: Suit
    rank: Rank

    def __str__(self):
        return f"{self.suit.name} {self.rank.name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.suit}, {self.rank})"
