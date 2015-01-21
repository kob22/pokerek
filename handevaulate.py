from deck import Deck
from card import Card
from hand import Hand
from enum import Enum
import collections


class Hand_E:
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

    def __init__(self,hand):
        self.hand=hand;

    def __str__(self):
        return self.hands[self.hand]


class HandEvaulate:
    def __init__(self, cards):
        self.hand = Hand(cards)
        self.cards = self.hand.cards
        self.pokerHand = 0


    def evaulate(self):
        straight = False
        flush = False
        flush_color = -1
        highCardStraight =0

        ranks = collections.Counter()
        suits = collections.Counter()

        print (self.cards)
        for card in self.cards:
            ranks[card.rank] += 1
            suits[card.suit] += 1

        countCards = len(ranks)
        countSuits = len(suits)

        #high card
        if countCards == 7:
            self.pokerHand=0
        #one pair
        elif countCards == 6:
            self.pokerHand=1
        #two pair
        elif countCards == 5:
            self.pokerHand=2
        elif countCards == 4:
            #four od kind
            if 4 in ranks.values():
                self.pokerHand=7
            #full
            elif 3 in ranks.values():
                self.pokerHand=6
            #three (dwie) todo
            elif 2 in ranks.values() and 1 in ranks.values():
                self.pokerHand=2
        elif countCards <4 and countCards >1:
            #four od kind
            if 4 in ranks.values():
                self.pokerHand=7
            #full
            elif 3 in ranks.values():
                self.pokerHand=6
        #error
        else:
            self.pokerHand=-1



        #flush 12345 6 7
        if countSuits <4 and suits.most_common(1)[0][1] >3 and self.pokerHand <5:
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
                while(is_it_ok and (i+j+1) < len(cardsR) ):
                    if (cardsR[i+j]+1) == (cardsR[i+j+1]):

                        highCardStraight = cardsR[i+j+1]

                        is_it_ok = True
                        if (j==3):

                            straight = True
                        j+=1
                    elif (j==3 and cardsR[0]== 2 and (14 in cardsR)):
                        is_it_ok = True
                        if (j==3):
                            highCardStraight = 5
                            straight = True
                        j+=1
                    else:
                        is_it_ok = False

                i+=1

        if straight and self.pokerHand <4:
            self.pokerHand = 4

        #todo brakuje sprawdzenia czy to to samo
        if flush and straight:
            isPoker = False
            isOk = True
            suits_straight = collections.Counter()

            if highCardStraight == 5:
                for x in range(highCardStraight,highCardStraight-4,-1):
                    suits_straight[self.get_card_suit(x)] += 1
                suits_straight[self.get_card_suit(14)] += 1
            else:
                for x in range(highCardStraight,highCardStraight-5,-1):
                    suits_straight[self.get_card_suit(x)] += 1

            if len(suits_straight) == 1:
                if highCardStraight == "14":
                    self.pokerHand = 9
                else:
                    self.pokerHand = 8


        hand_print = Hand_E(self.pokerHand)
        if self.pokerHand == 0:
            print(hand_print)
            print (self.high_card())
            return self.pokerHand
        elif self.pokerHand == 1:
            print(hand_print)
            return self.pokerHand
        elif self.pokerHand == 2:
            print(hand_print)
            return self.pokerHand
        elif self.pokerHand == 3:
            print(hand_print)
            return self.pokerHand
        elif self.pokerHand == 4:
            print(self.straight(highCardStraight))
            print(hand_print)
            return self.pokerHand
        elif self.pokerHand == 5:
            print(self.flush(flush_color))
            print(hand_print)
            return self.pokerHand
        elif self.pokerHand == 6:
            print(hand_print)
            return self.pokerHand
        elif self.pokerHand == 7:
            print(hand_print)
            return self.pokerHand
        elif self.pokerHand == 8:
            print(hand_print)
            return self.pokerHand
        elif self.pokerHand == 9:
            print(hand_print)
            return self.pokerHand
        elif self.pokerHand == -1:
            print ("BLAAAAAAAD!!!!!!!")
            return -1

    def get_card_suit(self,card_rank):
        for card in self.cards:
            if card.rank == card_rank:
                return card.suit

    def high_card(self):
        self.hand.sort_rank()
        return self.hand.cards[:5]

    def flush(self,flush_color):
        flush_hand_temp = Hand(self.hand.hand_in_color(flush_color))
        prv_card_rank=-1
        flush_hand=[]
        for card in flush_hand_temp.cards:
            if card.rank!= prv_card_rank:
                flush_hand.append(card)
            prv_card_rank=card.rank
        return flush_hand[:5]

    def straight(self,highCard):
        ranks = [card.rank for card in self.hand.cards]
        striaght = []
        prv_card_rank=-1
        ace_for_low=[]
        for card in self.hand.cards:
            if card.rank <= highCard:
                if prv_card_rank!=card.rank:
                    striaght.append(card)
            if card.rank == 14:
                ace_for_low=card.suit
            prv_card_rank=card.rank

        if highCard == 5:
            striaght.append(Card(14,ace_for_low))
        return striaght[:5]
