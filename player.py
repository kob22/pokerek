from hand import *

## @package class Player
#  klasa reprezentujaca gracza
#
#
class Player:

    ##konstruktor tworzacy gracza
    # @id gracza
    # @name nazwa gracza
    # @money budzet gracza
    def __init__(self,id,name, money):
        self.id = id
        self.name = "noname"
        self.money = money
        self.hand = Hand()
        self.isAllin = False
        self.isFold = False
        self.seat = 0
        self.action_n =-1
        self.bet_how = 0
        self.power_hand = -1
        self.best_hand = []

    ## metoda kopiujaca gracza
    def copy(self):
        other = Player(self.id, self.name, self.money)
        other.hand = self.hand.copy()
        return other

    ## metoda resetujaca parametry gracza do nastepnego rozdania
    def reset(self):
        self.hand = Hand()
        self.isAllin = False
        self.isFold = False
        self.action_n =-1
        self.bet_how = 0

    ## metoda placenia zetonami
    def pay(self,how_many):
        if(self.money - how_many > 0):
            self.money-=how_many
            self.bet_how+=how_many
            return how_many
        else:
            rest=self.money
            self.bet_how+=rest
            self.money = 0
            self.isAllin = True
            print ("allin")
            return rest

    ## metoda pokazujaca karty gracza
    def show_cards(self):
        return self.hand

    ## metoda licytacji, z niej wywoływane są poszczegolne akcje
    # @param do_it rodzaj kacji
    # @param bet ilosc zetonow
    # @param bet_prv poprzedni najwiekszy zaklad w rozdaniu
    def action(self,do_it, bet, bet_prv):
        action=-1
        answer =-1
        if(do_it=="check"):
            answer = self.check(bet_prv)
            action=0
        elif (do_it=="call"):
            answer = self.call(bet_prv)
            action=1
        elif (do_it=="bet"):
            answer = self.bet(bet_prv,bet)
            action=2
        elif (do_it=="raise"):
            answer = self.raisee(bet_prv,bet)
            action=3
        elif (do_it=="allin"):
            answer = self.allin(bet_prv)
            action=4
        elif (do_it=="fold"):
            answer = self.fold(bet_prv)
        return [answer,action]

    ## metoda do akcji allin
    def allin(self,bet_prv):
        return self.pay(self.money)

    ## metoda do akcji raise
    def raisee(self,bet_prv,raisee):
        if bet_prv > 0 and raisee > bet_prv:
            return self.pay(raisee-self.bet_how)
        else:
            return -1

    ## metoda do akcji check
    def check(self,bet_prv):
        if (bet_prv == 0 or bet_prv == self.bet_how):
            return 0
        else:
            return -1

    ## metoda do akcji bet
    def bet(self,bet_prv,bet):
        if (bet_prv == 0):
            return self.pay(bet)
        else:
            return -1

    ## metoda do akcji call
    def call(self,bet_prv):
        if bet_prv >0:
            return self.pay(bet_prv-self.bet_how)
        else:
            return self.check(bet_prv)

    ## metoda do akcji fold
    def fold(self,bet_prv):
        self.isFold = True
        return 0


