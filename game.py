from player import *
from deck import *
from hand import *
from handevaulate import *
class Game:

    def __init__(self,players):
        self.small_blind = 5
        self.big_blind = 10
        self.award = 0
        self.players = players
        self.deck = Deck()
        self.board = []
        self.bet=0
        self.stillInGame = [p.id for p in self.players ]
        print (self.stillInGame)


    def start(self):

        self.deck.shuffle()
        self.pay_blinds()

    def begin_turn(self):
        for two in range(2):
            for player in self.players:
                player.hand.add_card(self.deck.getOne())

    def auction(self):
        countPlayers= len(self.players)
        action = 0

        while(countPlayers>0):
            for player in self.players:
                print (player.isFold)
                if not player.isFold and not player.isAllin:
                    if player.action_n != action:
                        #print "action %d" % player.action_n
                        #print "action %d" % action
                        print ("Gracz %d ma kasy  %d" % (player.id, player.money))
                        print ("co robisz?")
                        answer = player.action(self.bet)
                        self.award+=answer[0]

                        if self.bet < answer[0]:
                        #    print "wchooodze"
                            action+=1
                            player.action_n = action
                            self.bet = answer[0]
                            countPlayers = len(self.players)
                        elif self.bet == answer[0]:
                            player.action_n = action
                for p in self.players:
                    print ("Gracz %d ma kasy  %d" % (p.money, p.bet_how))
                countPlayers-=1



    def flop(self):
        self.board.extend(self.deck.getCards(3))

    def turn(self):
        self.board.append(self.deck.getOne())

    def river(self):
        self.board.append(self.deck.getOne())

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


    def reset(self):
        for player in self.players:
            player.reset()


    def search_player(self, id):
        for player in self.players:
            if player.id == id:
                return player
        raise Exception("Not found")

    def winner_by_fold(self):
        print ("---------------------")
        for player in self.players:
            if player.id in self.stillInGame and player.isFold:
                print (self.stillInGame)
                print (player.id)
                self.stillInGame.remove(player.id)
        print ("---------------------")
        if len(self.stillInGame) == 1:

            return self.winner(self.stillInGame[0])
        return -1

    def winner(self,id):
        player = self.search_player(id)
        player.money+= self.award
        print ("wygral gracz %d" % player.id)
        self.reset()
        return 0

    def who_is_winner(self):
        winner = []
        max_power_hand = -1
        for player in self.players:
            if not player.isFold:

                power_hand = HandEvaulate(Hand(self.board, player.hand.cards).cards).evaulate()
                if power_hand > max_power_hand:
                    max_power_hand = power_hand
                    winner = []
                    winner.append(player)
                elif power_hand == max_power_hand:
                    winner.append(player)
        for win in winner:
            player = self.search_player(win.id)
            player.money+=self.award/len(winner)
            print ("wygral gracz %d" % player.id)
        self.reset()
        return 0

