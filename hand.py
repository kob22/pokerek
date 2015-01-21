from deck import Deck
from card import Card
class Hand:

    def __init__(self, cards1=[], cards2=[]):
        self.cards = []
        self.cards.extend(cards1)
        self.cards.extend(cards2)
        self.sort_rank()

    def show(self):
        print (self.cards)

    def sort_rank(self):
        self.cards.sort(key=lambda card: card.rank, reverse=True)

    def hand_in_color(self,flush_color):
        hand_in_color = [card for card in self.cards if card.suit == flush_color]
        return hand_in_color

    def sort_suit(self):
        self.cards.sort(key=lambda card: card.suit, reverse=True)

    def return_cards(self):
        return self.cards

    def add_card(self,card):
        self.cards.append(card)

    def __repr__(self):
        return "%s" % (self.cards)

    def copy(self):
        other = Hand()
        other.cards = [ x for x in self.cards ]
        return other