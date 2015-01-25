from deck import Deck
from card import Card

## @package class Hand
#  klasa reprezentujaca kilka kart
#
#
class Hand:
    ## Documentation for a construcktor.
    #  @cards1 lista kart
    #  @cards2 lista kart
    def __init__(self, cards1=[], cards2=[]):
        self.cards = []
        self.cards.extend(cards1)
        self.cards.extend(cards2)
        self.sort_rank()

    ## metoda pokazujaca reke
    def show(self):
        print (self.cards)

    ## metoda sortujaca malejaco reke
    def sort_rank(self):
        self.cards.sort(key=lambda card: card.rank, reverse=True)

    ## metoda zwracajaca reke w jednym kolorze
    def hand_in_color(self,flush_color):
        hand_in_color = [card for card in self.cards if card.suit == flush_color]
        return hand_in_color

    ## metoda sortujaca reke po kolorze
    def sort_suit(self):
        self.cards.sort(key=lambda card: card.suit, reverse=True)

    ## metoda zwracajaca karty
    def return_cards(self):
        return self.cards

    ## metoda dodajaca karte
    # @card karta
    def add_card(self,card):
        self.cards.append(card)

    ## metoda reprezentujaca reke
    def __repr__(self):
        return "%s" % (self.cards)

    ## metoda kopiujaca reke
    def copy(self):
        other = Hand()
        other.cards = [ x for x in self.cards ]
        return other