from hand import *
class Player:

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


    def copy(self):
        other = Player(self.id, self.name, self.money)
        other.hand = self.hand.copy()
        return other

    def reset(self):
        self.hand = Hand()
        self.isAllin = False
        self.isFold = False
        self.action_n =-1
        self.bet_how = 0

    def pay(self,how_many):
        if(self.money - how_many > 0):
            self.money-=how_many
            self.bet_how+=how_many
            return self.bet_how
        else:
            rest=self.money
            self.bet_how+=rest
            self.money = 0
            self.isAllin = True
            print ("allin")
            return self.bet_how

    def show_cards(self):
        return self.hand

    def action(self,bet_prv):

        action=-1
        answer =-1

        while(answer==-1):
            a="call"
            bet=0
            if(a=="check"):
                answer = self.check(bet_prv)
                action=0
            elif (a=="call"):
                answer = self.call(bet_prv)
                action=1
            elif (a=="bet"):
                answer = self.bet(bet_prv,bet)
                action=2
            elif (a=="raise"):
                answer = self.raisee(bet_prv,bet)
                action=3
            elif (a=="allin"):
                answer = self.allin(bet_prv)
                action=4
            elif (a=="fold"):
                self.fold(bet_prv)
                answer =0
                action=0
            print (answer)
        return [answer,action]

    def allin(self,bet_prv):
        return self.pay(self.money)

    def raisee(self,bet_prv,raisee):
        print ("raise")
        print (bet_prv)
        if bet_prv > 0 and raisee > bet_prv:
            return self.pay(raisee-self.bet_how)
        else:
            return -1

    def check(self,bet_prv):
        print (bet_prv)
        if (bet_prv == 0 or bet_prv == self.bet_how):
            return 0
        else:
            return -1


    def bet(self,bet_prv,bet):
        if (bet_prv == 0):
            return self.pay(bet)
        else:
            return -1

    def call(self,bet_prv):
        if bet_prv >0:
            return self.pay(bet_prv-self.bet_how)
        else:
            return self.check(bet_prv)


    def fold(self,bet_prv):
        if bet_prv == 0 or bet_prv == self.bet_how:
            self.check(bet_prv)
        else:
            self.isFold = True
            return 0

