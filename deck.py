'''Deck class creates and shuffles a list of card objects of size 52'''
from random import shuffle
from card import Card
from card import suits
from card import ranks

class Deck:
    '''deck class instantiates a list of 52 card objects'''
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # here we create the card object
                created_card = Card(suit, rank)

                #card is added to the all_cards list
                self.all_cards.append(created_card)

    def shuffle(self):
        '''shuffles the deck'''
        return shuffle(self.all_cards)

    def deal_one(self):
        '''utilises the pop() method to take one card from the list and return it in one go'''
        return self.all_cards.pop()



    def show_deck(self):
        '''show_deck iterates across the list of cards in a deck using the all_cards
           variable and prints them to console'''
        for card in self.all_cards:
            print(card)
