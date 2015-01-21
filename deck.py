from card import Card
import random
class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(1,5):
            for rank in range(2,15):
                self.cards.append(Card(rank,suit))
        self.totalCards = len(self.cards)
        
        if self.totalCards != 52:
            print ("blad")
            # sys.exit("ERROR: Invalid number of cards")
            

    
    def shuffle(self):
        random.shuffle(self.cards)        
        return self.cards
                  
    def show(self):
        print (self.cards)

    def getOne(self):
        return self.cards.pop()

    def getCards(self, numberCards):
        if numberCards > self.cardsLeft():
            return sys.exit("ERROR: Not enough cards")
        cardsReturn = []
        for card in range(numberCards):
            cardsReturn.append(self.cards.pop())
        return cardsReturn

    def cardsLeft(self):
        return len(self.cards)
