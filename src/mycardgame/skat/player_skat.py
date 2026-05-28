from mycardgame.cards import Card
from mycardgame.universal_game.player import Player

class PlayerSkat(Player):

    def __init__(self, name: str, hand: list[Card] = None):
        super().__init__(name, hand)
        self.won_cards = list[Card]()
        self.plays_solo = False
