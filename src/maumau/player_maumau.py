# from src.maumau.agent import Agent
from src.universal_game import Player
from src.cards import Card

class PlayerMauMau(Player):

    def __init__(self, name: str, hand: list[Card] = None):
        super().__init__(name, hand)
        self.won = False

    def maumau(self):
        self.won = True
