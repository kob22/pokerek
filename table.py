from deck import Deck
from card import Card
from hand import Hand
from handevaulate import HandEvaulate
from player import Player
from game import Game
import timeit

class Table:

    def __init__(self):
        self.players=[]

    def addPlayer(self,player):
        self.players.append(player)

    def removePlayer(self,player):
        print ("abc")

    def start(self):
        start = timeit.default_timer()

        game = Game(self.players)
        game.start()
        game.begin_turn()
        game.auction()

        if game.winner_by_fold() == 0:
            return 0
        for id in self.players:
            print (id.money)
            print (id.isFold)

        game.flop()
        print (game.board)
        game.auction()

        if game.winner_by_fold() == 0:
            return 0
        for id in self.players:
            print (id.money)
            print (id.isFold)


        game.turn()
        print (game.board)
        game.auction()

        if game.winner_by_fold() == 0:
            return 0
        for id in self.players:
            print (id.money)
            print (id.isFold)

        game.river()
        print (game.board)
        game.auction()

        if game.winner_by_fold() == 0:
            return 0

        for id in self.players:
            print (id.hand)
            print (id.money)
            print (id.isFold)

        if game.who_is_winner() == 0:
            return 0

        print (game.board)
        for id in players:
            print (id.hand)
            print (id.money)
            print (id.isFold)




        stop = timeit.default_timer()


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
