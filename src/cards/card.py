from .suit import Suit
from .rank import Rank

class Card:

    big_deck = False

    def __init__(self, suit: Suit, rank: Rank, big_deck=False) -> None:
        # instance check necessary??
        if not isinstance(suit, Suit):
            raise TypeError("suit must be a Suit Type")
        if not isinstance(rank, Rank):
            raise TypeError("rank must be a Rank Type")

        if not big_deck and rank.value < Rank.SEVEN.value:
            raise ValueError("rank lower than 7 is not allowed in a small deck")

        self.big_deck = big_deck
        self._suit = suit
        self._rank = rank


    def __str__(self) -> str:
        return f"{self.suit.name} {self.rank.name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.suit}, {self.rank})"

    @property
    def suit(self) -> Suit:
        return self._suit

    @suit.setter
    def suit(self, value: Suit):
        self._suit = value

    @property
    def rank(self) -> Rank:
        return self._rank

    @rank.setter
    def rank(self, value: Rank):
        if not self.big_deck and value.value < Rank.SEVEN.value:
            raise TypeError("rank lower than 7 is not allowed in a small deck")
        self._rank = value



