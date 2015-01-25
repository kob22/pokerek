from card import Card
import random

## @package class Deck
#  klasa reprezentujaca talie kart
#
#
class Deck:

    ##konstruktor, 52 karty
    def __init__(self):
        self.cards = []
        for suit in range(1,5):
            for rank in range(2,15):
                self.cards.append(Card(rank,suit))
        self.totalCards = len(self.cards)
        
        if self.totalCards != 52:
            print ("blad")
            # sys.exit("ERROR: Invalid number of cards")
            

    ## metoda tasujaca karty
    def shuffle(self):
        random.shuffle(self.cards)        
        return self.cards

    ## metoda pokazujaca talie kart
    def show(self):
        print (self.cards)

    ## metoda rozdajaca 1 karte
    def getOne(self):
        return self.cards.pop()

    ## metoda rozdajaca n kart
    def getCards(self, numberCards):
        if numberCards > self.cardsLeft():
            return sys.exit("ERROR: Not enough cards")
        cardsReturn = []
        for card in range(numberCards):
            cardsReturn.append(self.cards.pop())
        return cardsReturn

    ##metoda liczaca ilosc kart w talii
    def cardsLeft(self):
        return len(self.cards)
