from src.cards import Deck
from src.cards import Card
from src.maumau import PlayerMauMau




class GameBoard:
    def __init__(self, player_list: list[PlayerMauMau],
                 double_deck: bool=False, big_deck: bool=False):
        # create player
        self.player_list = player_list
        self.current_player = None

        # create deck
        self.deck = Deck(big_deck=big_deck, double_deck=double_deck)
        self.deck.create_new_deck()
        self.deck.shuffle()

        self.used_cards = list[Card]()

    # ----------- card actions ----------------
    # ASSUMPTION: only current player can draw cards, either because he
    # can't play any cards or because of action card
    # -> 7 (remember passing on with another 7)
    def deal_cards(self, amount: int=1, player: PlayerMauMau=None):
        if amount < 1:
            raise ValueError("Can't deal less than 1 cards")

        if player is None:
            # draw one or more cards for current player
            for i in range(amount):
                self.current_player.receive_card(self.deck.draw_card())
        else:
            for i in range(amount):
                player.receive_card(self.deck.draw_card())

    def setup_last_card(self):
        self.used_cards.append(self.deck.draw_card())

    def show_last_card(self):
        return self.used_cards[-1]


    def refill_deck(self):
        # TODO: refill deck with used cards (except last)
        pass



    # --------- player actions ------------------
    def play_card(self, card: Card):
        # player plays card
        self.current_player.play_card(card)
        # TODO: change current player to next player
        # effect should be applied by game engine, however change of
        # current_player should follow in this function, otherwise
        # no accurate game state, right? but could be awkward with game engine ...
        

    # TODO: player wins -> no longer in the game?
    # TODO: next players turn -> update current_player