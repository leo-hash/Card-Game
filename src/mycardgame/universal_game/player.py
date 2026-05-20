from src.mycardgame.cards import Card



class Player:

    def __init__(self, name: str, hand: list[Card] = None):
        self.name = name
        self.hand = hand
        if hand is None:
            self.hand = []


    def play_card(self, card: Card)->Card:
        if not self.hand.__contains__(card):
            raise ValueError(f"Card {card} not in hand")

        self.hand.remove(card)
        return card

    def receive_card(self, card: Card=None, card_list: list[Card] = None):
        if card is None and card_list is None:
            raise ValueError("Either a card or a list of cards is required")

        if card is not None and card_list is not None:
            raise ValueError("Too many arguments, either a card or a list of cards is required")

        if card is not None:
            self.hand.append(card)
        else:
            self.hand.extend(card_list)

    def __str__(self):
        return f"Player {self.name}"

    def __repr__(self):
        return f"Player {self.name}"