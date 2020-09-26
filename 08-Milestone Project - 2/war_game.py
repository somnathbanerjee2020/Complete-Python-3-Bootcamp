# War Game with Cards

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self,suits,ranks):
        self.suits = suits
        self.ranks = ranks



    def build_deck(suits, ranks):
        full_deck=[]
        for i in suits:
            for j in ranks:
                i_j=Card(i,j)
                print(i_j)
                full_deck.append(i_j)
        print(full_deck)
    
    def __str__(self):
        return Hello


#print(suits)
#print(ranks)

c1=Card(suits, ranks)


#print(c1)

#dddd=Deck()
#dddd.build_deck(suits, ranks)
