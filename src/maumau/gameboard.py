from src.cards import Deck
from src.cards import Card
from src.maumau import PlayerMauMau


class GameBoard:
    def __init__(self, player_list: list[PlayerMauMau],
                 big_deck: bool=False, double_deck: bool=False):
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
                self._pick_card(self.curr_player)
        else:
            for i in range(amount):
                self._pick_card(player)

    def _pick_card(self, player: PlayerMauMau):
        try:
            player.hand.append(self.deck.draw_card())
        # deck is empty
        except IndexError:
            # TODO: second IndexError would occur, if every card is currently used (except last card)
            self.refill_deck()
            player.hand.append(self.deck.draw_card())
            # alt. solution in deal_cards: i--, but could lead to infinite loop
            # second index error not handled, but if it accurses,
            # there is a serious problem with refill_deck() ->
            # Error should be communicated


    def setup_last_card(self):
        self.used_cards.append(self.deck.draw_card())

    def show_last_card(self):
        return self.used_cards[-1]

    def refill_deck(self):
        if len(self.used_cards) <= 0:
            raise ValueError("Deck not properly refilled, self.used_cards is empty")
        self.deck.add_card(card_list=self.used_cards[:-1])
        self.deck.shuffle()
        del self.used_cards[:-1]


    # --------- player actions ------------------
    def play_card(self, card: Card):
        # player plays card
        self.used_cards.append(self.curr_player.play_card(card))

    #  next players turn -> update current_player
    def move_to_next_player(self):
        self.curr_player = self.next_player()

    # player wins -> no longer in the game?
    # returns true if game ends
    def check_player_wins(self)->bool:
        if len(self.curr_player.hand) <= 0:
            print(f"Player {self.curr_player.name} has won!")
            self.player_list.remove(self.curr_player)
            if len(self.player_list) <= 1:
                print(f"Game Over")
                return True
            return False
        return False


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