from .suit import Suit
from .rank import Rank

class Card:

    def __init__(self, suit: Suit, rank: Rank) -> None:
        # instance check necessary??
        if not isinstance(suit, Suit):
            raise TypeError("suit must be a Suit Type")
        if not isinstance(rank, Rank):
            raise TypeError("rank must be a Rank Type")


        self.suit = suit
        self.rank = rank


    def __str__(self) -> str:
        return f"{self.suit.name} {self.rank.name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.suit}, {self.rank})"

    def __eq__(self, other) -> bool:
        return self.suit == other.suit and self.rank == other.rank

