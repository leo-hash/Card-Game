from .rank import Rank
from .suit import Suit
from .card import Card

import random

class Deck:
    big_deck = False
    double_deck = False

    def __init__(self, big_deck=False, double_deck=False):
        self.cards = []
        self.big_deck = big_deck
        self.double_deck = double_deck

    def create_new_deck(self):
        # create card deck depending on parameters(small/big deck, double deck, ...)
        # inheritance vs. parametrisation
        # only during creation relevant, no behavioral change because of different deck size

        for suit in Suit:
            for rank in Rank:
                if (not self.big_deck) and (rank.value < 7):
                    continue

                self.add_card(Card(suit, rank, self.big_deck))
                if self.double_deck:
                    self.cards.append(Card(suit, rank, self.big_deck))

    def add_card(self, card: Card=None, card_list: list[Card] = None):
        if card is None and card_list is None:
            raise ValueError("Either a card or a list of cards is required")

        if card is not None and card_list is not None:
            raise ValueError("Too many arguments, either a card or a list of cards is required")

        if card is not None:
            if not card.big_deck == self.big_deck:
                raise ValueError("Deck type not allowed, card.big_deck must be equal to deck.big_deck ")
            # skip rank 2 to 6 if small deck
            if self.big_deck or card.rank.value >= 7:
                self.cards.append(card)

        else:
            for card in card_list:
                if not card.big_deck == self.big_deck:
                    raise ValueError("Deck type not allowed, card.big_deck must be equal to deck.big_deck ")
                if self.big_deck or card.rank.value >= 7:
                    self.cards.append(card)


    def shuffle(self, seed=None):
        # randomly shuffle deck, seed may dependent on time, but reproducible
        if seed is not None:
            # shuffle with seed
            random.Random(seed).shuffle(self.cards)
        else:
            # shuffle without seed
            random.shuffle(self.cards)

    def draw_card(self)->Card:
        # draw one card from the top of the deck
        return self.cards.pop(0)

    # def show_last_card(self)->Card:
    #     # show last added card
    #     return self.cards[-1]

