from mycardgame.universal_game import Player
from mycardgame.cards import Card

class PlayerMauMau(Player):

    def __init__(self, name: str, hand: list[Card] = None):
        super().__init__(name, hand)
        self.won = False


