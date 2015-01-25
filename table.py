from deck import Deck
from card import Card
from hand import Hand
from handevaulate import HandEvaulate
from player import Player
from game import Game
import timeit

## @package class Table
#  klasa reprezentujaca stolik
#
#
class Table:

    ## konstruktor
    def __init__(self):
        self.players=[]
        self.game = Game(self.players)

    ## dodawanie gracza
    # @param player
    def addPlayer(self,player):
        self.players.append(player)

    #def removePlayer(self,player):
        #print ("abc")

    ## start gry na stoliku
    def start(self):
        self.game = Game(self.players)
        self.game.start()
        self.game.begin_turn()
        return 0

    ## licytacja, zwraca [ , ] pierwszy parametry sprawdza ile jeszcze graczy ma licytowac, drugi w przypadku -1 odpowiedz gracza jest bledna, >=0 jest poprawna
    ## przyjmuje id gracza, akcje np "fold" "call" "bet" "raise" oraz wysokosc zakladu
    # @param id gracza
    # @param action co wykonac
    # @param bet wysokosc zakladu
    def auction(self,id,action,bet):
        print (action)
        return self.game.auction(id,action,bet)

    ## drukowanie kart na stole
    def board(self):
        return self.game.board

    ## drukowanie graczy
    def print_players(self):
        for id in self.players:
            print (id.money)
            print (id.isFold)

    ## drukowanie kart graczy
    def print_players_hand(self):
        for id in self.players:
            print (id.hand)
            print (id.money)
            print (id.isFold)

    ## graj flop
    def play_flop(self):
        self.game.flop()
        return 0

    ## graj turn
    def play_turn(self):
        self.game.turn()
        return 0

    ## graj river
    def play_river(self):
        self.game.river()
        return 0

    ## dodaj gracza
    # @param id gracza
    # @param money ilosc kasy
    def add_players(self,id,money):
        self.addPlayer((Player(id,"{0}".format(id), money) ))
        return 0

    ## sprawdza czy jest wygrany, jesli tak zwraca 0
    def is_winner(self):
        if self.game.winner_by_fold() == 0:
            return 0
        return -1

    ## sprawdza czy jest wygrany, jesli licytacja jest skonczona, jesli tak zwraca 0
    def is_winner_after_river(self):
        if self.game.who_is_winner() == 0:
            return 0
        return -1


# czworka =0
# poker = 0
# x = 0
# for a in range(10):
#     x = Deck()
#     x.shuffle()
#     table = x.getCards(5)
#     player = x.getCards(2)
#     ha = Hand(table, player)
#     o = HandEvaulate(ha.cards)
#     m = o.cojest()
#     if m == 1:
#         czworka+=1
#     elif m == 2:
#         poker+=1
#
#     if a == 99999999:
#         print "all :)"
# print x.totalCards
# table = [Card(2,1), Card(3,2), Card(4,1), Card(5,2), Card(6,3)]
# player = [Card(7,4), Card(7,2)]
# ha = Hand(table, player)
#
# o = HandEvaulate(ha.cards)
# o.cojest()
#
# table = [Card(2,1), Card(2,2), Card(4,1), Card(5,2), Card(6,3)]
# player = [Card(7,4), Card(7,2)]
# ha = Hand(table, player)
#
# o = HandEvaulate(ha.cards)
# o.cojest()
#
# table = [Card(2,1), Card(2,2), Card(3,1), Card(3,2), Card(6,3)]
# player = [Card(7,4), Card(7,2)]
# ha = Hand(table, player)
#
# o = HandEvaulate(ha.cards)
# o.cojest()
#
# table = [Card(2,1), Card(2,2), Card(3,1), Card(3,2), Card(4,3)]
# player = [Card(4,4), Card(7,2)]
# ha = Hand(table, player)
#
# o = HandEvaulate(ha.cards)
# o.cojest()
#
# table = [Card(2,1), Card(2,2), Card(2,1), Card(5,2), Card(6,3)]
# player = [Card(7,4), Card(7,2)]
# ha = Hand(table, player)
#
# o = HandEvaulate(ha.cards)
# o.cojest()
#
# table = [Card(2,1), Card(2,2), Card(2,1), Card(3,2), Card(3,3)]
# player = [Card(3,4), Card(7,2)]
# ha = Hand(table, player)
#
# o = HandEvaulate(ha.cards)
# o.cojest()
#
# table = [Card(2,1), Card(2,2), Card(2,1), Card(3,2), Card(3,3)]
# player = [Card(7,4), Card(7,2)]
# ha = Hand(table, player)
#
# o = HandEvaulate(ha.cards)
# o.cojest()
#
# table = [Card(2,1), Card(3,2), Card(4,1), Card(5,2), Card(6,3)]
# player = [Card(7,4), Card(8,2)]
# ha = Hand(table, player)
#
# o = HandEvaulate(ha.cards)
# o.cojest()
#
# table = [Card(2,2), Card(3,2), Card(4,2), Card(5,2), Card(2,2)]
# player = [Card(14,2), Card(8,2)]
# ha = Hand(table, player)
#
# o = HandEvaulate(ha.cards)
# o.cojest()
#
# table = [Card(3,2), Card(4,2), Card(5,2), Card(6,2), Card(6,3)]
# player = [Card(6,4), Card(8,2)]
# ha = Hand(table, player)
#
# o = HandEvaulate(ha.cards)
# o.cojest()
