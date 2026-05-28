from mycardgame.cards import Deck, Card


class GameBoardSkat:

    def __init__(self, player_list):
        self.player_list = player_list
        self.skat = list[Card]()
        self.current_stich = list[Card]()


        self.deck = Deck(big_deck=False, double_deck=False)
        self.deck.create_new_deck()
        self.deck.shuffle()