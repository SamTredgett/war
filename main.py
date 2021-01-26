'''game set up and main loop body for the war game'''
from time import sleep
from player import Player
from deck import Deck


# Game setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

print(player_one)
print(player_two)

GAME_ON = True
AT_WAR = False
ROUND_NUM = 0
cards_on_table = []

#Main game loop
while GAME_ON:
    while not AT_WAR:
        cards_on_table = []
        ROUND_NUM += 1
        print(f'Round {ROUND_NUM}')
        print(player_one)
        print(player_two)
        player_one.shuffle_hand()
        player_two.shuffle_hand()
        # Check to see if a player has run out of cards to end the game
        if len(player_one.all_cards) == 0:
            print('Player One has lost the game!')
            GAME_ON = False
            break
        if len(player_two.all_cards) == 0:
            print('Player Two has lost the game!')
            GAME_ON = False
            break
        else:
        # in this case, both players are still playing
            # places both cards into the X and Y variables (this is considered the in-play zone)
            X = player_one.remove_one()
            Y = player_two.remove_one()
            
            if X.value > Y.value:
                # Player one's card has greater value, both cards are added to player one's hand
                cards_on_table.append(X)
                cards_on_table.append(Y)
                for n in cards_on_table:
                    print( n)
                player_one.all_cards.extend(cards_on_table)
            elif Y.value > X.value:
                # Player two's card has greater value, both cards are added to player two's hand 
                cards_on_table.append(X)
                cards_on_table.append(Y)
                for n in cards_on_table:
                    print( n)
                player_two.all_cards.extend(cards_on_table)
            else:
                #this case means that the cards on the table hold the same value
                print("WAR!!!")
                AT_WAR = True
                print(X)
                print(Y)
                cards_on_table.append(X)
                cards_on_table.append(Y)

                while AT_WAR:
                    X = player_one.remove_one()
                    Y = player_two.remove_one()
                    print(X)
                    print(Y)
                    
                    if X.value > Y.value:
                        # Player one's card has greater value, both cards are added to player one's hand
                        cards_on_table.append(X)
                        cards_on_table.append(Y)
                        
                        player_one.all_cards.extend(cards_on_table)
                        AT_WAR = False
                    elif Y.value > X.value:
                        # Player two's card has greater value, both cards are added to player two's hand 
                        cards_on_table.append(X)
                        cards_on_table.append(Y)                        
                        player_two.all_cards.extend(cards_on_table)
                        AT_WAR = False
                    else:
                        #this case means that the cards on the table hold the same value
                        print("WAR!!!")
                        cards_on_table.append(X)
                        cards_on_table.append(Y)
