'''The player module provides several functionalities, it allows the player to have a hand,
 it allows them to change this hand on the go and interact with the deck in many ways.  '''
from random import shuffle
class Player:
    '''the player class has several functions which allow for the
    exchanging of card objects between different lists'''
    def __init__(self, name):
        '''creates a player object, player has a name and the attribute
        all_cards, list of card objects'''
        self.name = name
        self.all_cards = []

    def remove_one(self):
        '''remove one removes a card from the players hand'''
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        '''add_cards either appends a singular card won or merges
        a list of cards won to the players hand'''
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def shuffle_hand(self):
        '''shuffles the players hand'''
        shuffle(self.all_cards)

    def __str__(self):
        '''modifies the string method for the player class to display details about the player'''
        return f'Player {self.name} has {len(self.all_cards)} cards'
