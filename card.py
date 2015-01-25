## @package class Card
#  podstawowa klasa reprezentujaca karte
#
#
class Card:

    ## @var rank
    #  statyczna zmienna, reprezentuje figurę karty
    ranks = {
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "J",
        12: "Q",
        13: "K",
        14: "A"
    }
    ## @var suits
    # statyczna zmienna, reprezentuje kolor karty
    suits = {
        1: "s",
        2: "h",
        3: "d",
        4: "c"
    }
    ## Documentation for a construcktor.
    #  @param self wskaznik na siebie
    #  @param rank okresla figurę karty
    #  @param suit okresla kolor karty
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    ## Documentation for a method repr.
    #  @param self wskaznik na siebie
    # zwraca obiekt string reprezentujacy karte
    def __repr__(self):
        return '{0}{1}'.format(self.ranks[self.rank], self.suits[self.suit])
