from deck import Deck
from card import Card
from hand import Hand
from enum import Enum
import collections

## @package class Hand_e
#  klasa okreslajaca reke i reprezentatywna
#
#
class Hand_E:

    ## @var hands statyczna z rodzajami rąk
    hands = {
        0: "High Card",
        1: "One Pair",
        2: "Two Pair",
        3: "Three of a kind",
        4: "Straight",
        5: "Flush",
        6: "Full house",
        7: "Four of a kind",
        8: "Straight flush",
        9: "Royal flush"
    }

    ## kontruktor
    # @param hand ręka kart
    def __init__(self,hand):
        self.hand=hand;

    ## metoda reprezentujaca
    def __str__(self):
        return self.hands[self.hand]


## @package class HandEvaulate
#  klasa okreslajaca reke i reprezentatywna
#
#
class HandEvaulate:

    ## kontruktor
    # @param cards karty
    def __init__(self, cards):
        self.hand = Hand(cards)
        self.cards = self.hand.cards
        self.pokerHand = 0

    ## metoda okreslajaca sile reki
    def evaulate(self):
        straight = False
        flush = False
        flush_color = -1
        highCardStraight =-1
        most_common = -1
        pair=[]
        pairs = []
        three = []
        ranks = collections.Counter()
        suits = collections.Counter()

        print (self.cards)
        for card in self.cards:
            ranks[card.rank] += 1
            suits[card.suit] += 1

        countCards = len(ranks)
        countSuits = len(suits)
        most_common = ranks.most_common(1)[0][0]

        #high card
        if countCards == 7:
            self.pokerHand=0
        #one pair
        elif countCards == 6:
            pair = most_common
            self.pokerHand=1
        #two pair
        elif countCards == 5:
            if 3 in ranks.values():
                self.pokerHand = 3
            else:
                self.pokerHand=2
                pairs = [rank[0] for rank in ranks.most_common(2) if rank[1]==2]
        elif countCards == 4:
            #four od kind
            if 4 in ranks.values():
                self.pokerHand=7
            #full
            elif 3 in ranks.values():
                three = [rank[0] for rank in ranks.most_common(1) if rank[1] == 3]
                pairs = [rank[0] for rank in ranks.most_common(3) if rank[1] == 2]
                self.pokerHand=6
            #three (dwie) todo
            elif 2 in ranks.values() and 1 in ranks.values():
                pairs = [rank[0] for rank in ranks.most_common(3) if rank[1] == 2]
                self.pokerHand=2
        elif countCards <4 and countCards >1:
            #four od kind
            if 4 in ranks.values():
                self.pokerHand=7
            #full
            elif 3 in ranks.values():
                three = [rank[0] for rank in ranks.most_common(2) if rank[1] == 3]
                pairs = [rank[0] for rank in ranks.most_common(3) if rank[1] == 2]
                self.pokerHand=6
        #error
        else:
            self.pokerHand=-1



        #flush
        if countSuits <4 and suits.most_common(1)[0][1] ==5 and self.pokerHand <5:
            flush_color =suits.most_common(1)[0][0]
            self.pokerHand = 5
            flush = True

        #strit
        if countCards > 4:
            cardsR = list(ranks)
            cardsR.sort()
            straight = False
            i=0
            while((not straight) and i<3):
                is_it_ok = True
                j=0
                while(is_it_ok and (i+j+1) < len(cardsR) and not straight ):
                    if (cardsR[i+j]+1) == (cardsR[i+j+1]):

                        highCardStraight = cardsR[i+j+1]

                        is_it_ok = True
                        if (j==3):

                            straight = True
                        j+=1
                    elif (j==3 and cardsR[0]== 2 and (14 in cardsR) and highCardStraight==5 and is_it_ok):
                        is_it_ok = True
                        if (j==3):
                            highCardStraight = 5
                            straight = True
                        j+=1
                    else:
                        is_it_ok = False
                        highCardStraight=-1



                i+=1
        #strit
        if straight and self.pokerHand <4:
            self.pokerHand = 4

        #sprawdza czy poker
        if flush and straight:
            isPoker = False
            isOk = True
            suits_straight = collections.Counter()

            if highCardStraight == 5:
                for x in range(highCardStraight,highCardStraight-4,-1):
                    suits_straight[self.search_card_suit(x,flush_color)] += 1
                suits_straight[self.search_card_suit(14,flush_color)] += 1
            else:
                for x in range(highCardStraight,highCardStraight-5,-1):
                    suits_straight[self.search_card_suit(x,flush_color)] += 1
            if len(suits_straight) == 1 and suits_straight.most_common(1)[0][1]==5:
                if highCardStraight == 14:
                    self.pokerHand = 9
                else:
                    self.pokerHand = 8

        #na podstawie okreslonej reki wywoluje metode do znalezienia tej reki
        if self.pokerHand == 0:
            return (self.pokerHand, self.high_card())
        elif self.pokerHand == 1:
            return (self.pokerHand, self.one_pair(pair))
        elif self.pokerHand == 2:
            return (self.pokerHand, self.two_pair(pairs))
        elif self.pokerHand == 3:
            return (self.pokerHand, self.three_of_kind(most_common))
        elif self.pokerHand == 4:
            return (self.pokerHand,self.straight(highCardStraight))
        elif self.pokerHand == 5:
            return (self.pokerHand,self.flush(flush_color))
        elif self.pokerHand == 6:
            return (self.pokerHand, self.full_haouse(three, pairs))
        elif self.pokerHand == 7:
            return (self.pokerHand,self.four_kind(most_common))
        elif self.pokerHand == 8:
            return (self.pokerHand,self.straight_flush(highCardStraight,flush_color))
        elif self.pokerHand == 9:
            return (self.pokerHand,self.royal_flush(highCardStraight,flush_color))
        elif self.pokerHand == -1:
            print ("BLAAAAAAAD!!!!!!!")
            return (-1,[])

    ## zwraca kolor karty
    def get_card_suit(self,card_rank):
        for card in self.cards:
            if card.rank == card_rank:
                return card.suit

    ## szuka karty o podanej figurze i kolorze
    def search_card_suit(self,card_rank,card_suit):
        for card in self.cards:
            if card.rank == card_rank and card.suit==card_suit:
                return card.suit

    ## zwraca reke o wysokiej karcie
    def high_card(self):
        self.hand.sort_rank()
        return self.hand.cards[:5]

    ## zwraca reke o jednej parze
    def one_pair(self,pair):
        onepair = []
        temp=[]
        self.hand.sort_rank()
        i=0
        for card in self.hand.cards:

            if card.rank==pair:
                onepair.append(card)
            elif i<3:
                temp.append(card)
                i+=1
        onepair.extend(temp)
        return onepair

    ## zwraca reke z dwiema parami
    def two_pair(self,pairs):
        pairs.sort(reverse=True)
        pairs = pairs[:2]
        twopair= []
        temp=[]
        self.hand.sort_rank()
        i=0
        for card in self.hand.cards:
            if card.rank in pairs:
                twopair.append(card)
            elif i<1:
                temp.append(card)
                i+=1
        twopair.extend(temp)
        return twopair

    ## zwraca reke z trojka
    def three_of_kind(self,three):
        three_of_kind = []
        temp=[]
        self.hand.sort_rank()
        i=0
        for card in self.hand.cards:
            if card.rank==three:
                three_of_kind.append(card)
            elif i<2:
                temp.append(card)
                i+=1
        three_of_kind.extend(temp)
        return three_of_kind

    ## zwraca reke ze stritem
    def straight(self,highCard):
        ranks = [card.rank for card in self.hand.cards]
        straight = []
        prv_card_rank=-1
        ace_for_low=[]
        for card in self.hand.cards:
            if card.rank <= highCard:
                if prv_card_rank!=card.rank:
                    straight.append(card)
            if card.rank == 14:
                ace_for_low=card.suit
            prv_card_rank=card.rank

        if highCard == 5:
            straight.append(Card(14,ace_for_low))
        return straight[:5]

    ## zwraca reke z kolorem
    def flush(self,flush_color):
        flush_hand_temp = Hand(self.hand.hand_in_color(flush_color))
        print (flush_hand_temp.cards)
        prv_card_rank=-1
        flush_hand=[]
        for card in flush_hand_temp.cards:
            if card.rank!= prv_card_rank:
                flush_hand.append(card)
            prv_card_rank=card.rank
        return flush_hand[:5]

    ## zwraca reke z full
    def full_haouse(self,three, pairs):
        full = []
        temp = []
        self.hand.sort_rank()
        if len(three) >1:
            pairs.append(min(three))
        three = max(three)

        pairs = max(pairs)

        for card in self.hand.cards:
            if card.rank==three:
                full.append(card)
            elif card.rank == pairs:
                temp.append(card)
        full.extend(temp)
        return full[:5]

    ## zwraca reke z czworka
    def four_kind(self,most_common):
        four_kind=[]
        max_card=Card(0,0)
        for card in self.cards:
            if card.rank == most_common:
                four_kind.append(card)
            elif card.rank > max_card.rank:
                max_card = card
        four_kind.append(max_card)
        return four_kind

    ## zwraca reke z straight flush
    def straight_flush(self,highCard,flush_color):
        ranks = [card.rank for card in self.hand.cards]
        striaght = []
        prv_card_rank=-1
        ace_for_low=[]
        for card in self.hand.cards:
            if card.rank <= highCard:
                if prv_card_rank!=card.rank and card.suit == flush_color:
                    striaght.append(card)
                    prv_card_rank=card.rank
            if card.rank == 14:
                ace_for_low=card.suit


        if highCard == 5:
            striaght.append(Card(14,ace_for_low))
        return striaght[:5]

    ## zwraca reke z pokerem
    def royal_flush(self,highCard,flush_color):
        return self.straight_flush(highCard,flush_color)


