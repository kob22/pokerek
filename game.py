from player import *
from deck import *
from hand import *
from handevaulate import *
## @package class Game
#  klasa gry
#
#
class Game:
    ##konstruktor
    # @param gracze
    def __init__(self,players):
        self.small_blind = 5
        self.big_blind = 10
        self.award = 0
        self.players = players
        self.deck = Deck()
        self.board = []
        self.bet=0
        self.stillInGame = []
        self.countPlayers= len(self.players)
        self.action = 0

    ## metoda rozpycznajaca gre
    def start(self):
        self.stillInGame = [p.id for p in self.players ]
        self.deck.shuffle()
        self.pay_blinds()
        return 0

    ## losowanie kart
    def begin_turn(self):
        for two in range(2):
            for player in self.players:
                player.hand.add_card(self.deck.getOne())

    ## licytacja dla gracza
    # @param self
    # @param id gracza
    # @param do_it rodzaj akcji
    # @param wysokosc zakladu
    def auction(self,id,do_it,bet):
        answer = -1
        for playerf in self.players:
            if playerf.id == id:
                player = playerf
        if not player.isFold and not player.isAllin:
            if not player.isFold and not player.isAllin:

                if player.action_n != self.action:
                        #print "action %d" % player.action_n
                        #print "action %d" % action
                    #print ("Gracz %d ma kasy  %d" % (player.id, player.money))
                    #print ("co robisz?")

                    answer = player.action(do_it,bet,self.bet)
                    self.award+=answer[0]
                    if self.bet < answer[0]:
                        #    print "wchooodze"
                        self.action+=1
                        player.action_n = self.action
                        self.bet = answer[0]
                        countPlayers = len(self.players)
                    elif self.bet == answer[0]:
                        player.action_n = self.action
                self.countPlayers-=1

                if self.countPlayers == 0:
                    self.bet = 0
                    self.countPlayers = len(self.players)
                    self.action = 0
            else: answer=0
        return self.countPlayers,answer

    ## wykladanie kart flop
    def flop(self):
        self.board.extend(self.deck.getCards(3))

    ## wykladanie kart turn
    def turn(self):
        self.board.append(self.deck.getOne())

    ## wykladanie kart river
    def river(self):
        self.board.append(self.deck.getOne())

    ## placenie blinds
    def pay_blinds(self):
        countPlayers = len(self.players)
        if countPlayers>2:
            self.players[countPlayers-3].pay(self.small_blind)
            self.award+=self.small_blind
            self.players[countPlayers-2].pay(self.big_blind)
            self.award+=self.big_blind
        else:
            self.players[0].pay(self.small_blind)
            self.award+=self.small_blind
            self.players[1].pay(self.big_blind)
            self.award+=self.big_blind
        self.bet = self.big_blind

    ## reset graczy
    def reset(self):
        for player in self.players:
            player.reset()

    ## wyszukiwanie gracza
    # @param id gracza
    def search_player(self, id):
        for player in self.players:
            if player.id == id:
                return player
        raise Exception("Not found")

    ## sprawdzenie czy jest wygrany, jesli reszta zrezygnowala
    def winner_by_fold(self):
        for player in self.players:
            if player.id in self.stillInGame and player.isFold:

                self.stillInGame.remove(player.id)
        if len(self.stillInGame) == 1:
            return self.winner(self.stillInGame[0])
        return -1

    ## okreslenie wygranego
    def winner(self,id):
        player = self.search_player(id)
        player.money+= self.award
        self.reset()
        return 0

    ## sprawdzenie kto wygral na podstawie rąk, po river
    def who_is_winner(self):
        winner = []
        max_power_hand = -1
        for player in self.players:
            if not player.isFold:

                player.power_hand, player.best_hand = HandEvaulate(Hand(self.board, player.hand.cards).cards).evaulate()
                if player.power_hand > max_power_hand:
                    max_power_hand = player.power_hand
                    winner = []
                    winner.append(player)
                elif player.power_hand == max_power_hand:
                    winner.append(player)

        for win in winner:
            player = self.search_player(win.id)
            player.money+=self.award/len(winner)
            hand_print = Hand_E(player.power_hand)
            print ("%d wygral gracz %d z %s %s" % (self.award/len(winner), player.id, hand_print, player.best_hand))
        self.reset()
        return 0

