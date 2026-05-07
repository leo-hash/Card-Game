from src.cards import Deck
from src.cards import Card
from src.maumau import PlayerMauMau


class GameBoard:
    def __init__(self, player_list: list[PlayerMauMau],
                 double_deck: bool=False, big_deck: bool=False):
        # create player
        self.player_list = player_list
        self._curr_player_index = None
        self._curr_player = None

        # create deck
        self.deck = Deck(big_deck=big_deck, double_deck=double_deck)
        self.deck.create_new_deck()
        self.deck.shuffle()

        self.used_cards = list[Card]()


    # ----------- card actions ----------------
    def deal_cards(self, amount: int=1, player: PlayerMauMau=None):
        if amount < 1:
            raise ValueError("Can't deal less than 1 cards")

        if player is None:
            # draw one or more cards for current player
            for i in range(amount):
                self.curr_player.hand.append(self.deck.draw_card())
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
        self.used_cards.append(self.curr_player.play_card(card))

    #  next players turn -> update current_player
    def move_to_next_player(self):
        self.curr_player = self.next_player()

    # TODO: player wins -> no longer in the game?


    # ---------- player management/support methods-----------
    def next_player(self):
        return self.player_list[self._next_player_index()]

    def _next_player_index(self):
        if self._curr_player_index + 1 >= len(self.player_list):
            return 0
        return self._curr_player_index + 1

    @property
    def curr_player(self)->PlayerMauMau:
        return self._curr_player

    @curr_player.setter
    def curr_player(self, player):
        self._curr_player = player
        for i, curr in enumerate(self.player_list):
            if curr is player:
                self._curr_player_index = i
                break