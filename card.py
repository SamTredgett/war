'''this is the card class, it creates card objects which have a suit,
 rank and value(integer) for easy access'''

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three','Four', 'Five', 'Six','Seven','Eight','Nine','Ten','Jack','Queen','King', 'Ace')


class Card:
    '''Card class has initialiser to assign suit and rank,
    pulling value from the values global variable'''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
