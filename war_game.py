import random
import os
os.system('cls')

#assign card list
entire_deck_of_cards = ['QS', 'KS', 'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AH', '2H', '3H', '4H','AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS',  '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH']

#Shuffle the entire deck cards before game starts
random.shuffle(entire_deck_of_cards)

#Declare players decks before hand
clinton_deck = []
trump_deck = []

#Share the entire deck equally between the two players
while len(entire_deck_of_cards) !=0:
    clinton_deck.append(entire_deck_of_cards[0])
    entire_deck_of_cards.remove(entire_deck_of_cards[0])
    trump_deck.append(entire_deck_of_cards[0])
    entire_deck_of_cards.remove(entire_deck_of_cards[0])

#Declare Game Variables
continue_game = 'Y' #For Unless the player wants to end early
clinton_card_value = 0 #Worth of cards while fighting
trump_card_value = 0
clinton_final_deck = [] #Final list of the cards each player has at the end
trump_final_deck = []
tie_dump = [] #List cards lost by both contestant
rounds = 0 #Round counter

#Wait for user's input before proceeding with the game
continue_game = input("Do you want to proceed? Enter Y/N?\n")

#While loop Starts Here
while len(clinton_deck) != 0 and len(trump_deck) != 0 and (continue_game == 'y' or continue_game == 'Y'):
#Prints the stats of the game
    print ("Round " + str(rounds))
    print('_____________________________________________________________________________________')
    print ("                    " + "Card Played" + "           " + "Cards left" + "            " + "Cards won")
    print('-------------------------------------------------------------------------------------')
    print ('{0: <22}'.format("Clinton") +  '{0: <23}'.format(clinton_deck[0]) + '{0: <20}'.format(str(len(clinton_deck))) + '{0: <17}'.format(str(len(clinton_final_deck))))
    print('-------------------------------------------------------------------------------------')
    print ('{0: <22}'.format("Trump")+  '{0: <23}'.format(trump_deck[0]) + '{0: <20}'.format(str(len(trump_deck))) + '{0: <17}'.format(str(len(trump_final_deck))))
    print('-------------------------------------------------------------------------------------')
  
	

#Rules to check the worth of each player's cards
    if len(clinton_deck) != 0:
        if clinton_deck[0][0] == 'A' and trump_deck[0][0] == 'K':
             clinton_card_value = 14
        elif clinton_deck[0][0] == 'A' and trump_deck[0][0] != 'K':
            clinton_card_value = 1
        elif clinton_deck[0][0] == 'T':
            clinton_card_value = 10
        elif clinton_deck[0][0] == 'J':
            clinton_card_value = 11
        elif clinton_deck[0][0] == 'Q':
            clinton_card_value = 12
        elif clinton_deck[0][0] == 'K':
            clinton_card_value = 13
        else:
            clinton_card_value = int(clinton_deck[0][0])
    if len(trump_deck) != 0:
        if trump_deck[0][0] == 'A' and clinton_deck[0][0] == 'K':
             trump_card_value = 14
        elif trump_deck[0][0] == 'A' and clinton_deck[0][0] != 'K':
            trump_card_value = 1
        elif trump_deck[0][0] == 'T':
            trump_card_value = 10
        elif trump_deck[0][0] == 'J':
            trump_card_value = 11
        elif trump_deck[0][0] == 'Q':
            trump_card_value = 12
        elif trump_deck[0][0] == 'K':
            trump_card_value = 13
        else:
            trump_card_value = int(trump_deck[0][0])

#Check the cards played by the two contestants to decide who won the round.
    if clinton_card_value > trump_card_value:
        clinton_final_deck.append(trump_deck[0])
        trump_deck.remove(trump_deck[0])
        clinton_final_deck.append(clinton_deck[0])
        clinton_deck.remove(clinton_deck[0])
        print ("Winner             Clinton")
        print('_____________________________________________________________________________________\n\n\n') 
    if clinton_card_value < trump_card_value:
        trump_final_deck.append(clinton_deck[0])
        clinton_deck.remove(clinton_deck[0])
        trump_final_deck.append(trump_deck[0])
        trump_deck.remove(trump_deck[0])
        print ("Winner:             Trump")
        print('_____________________________________________________________________________________\n\n\n')  
    if clinton_card_value == trump_card_value:
        tie_dump.append(clinton_deck[0])
        tie_dump.append(trump_deck[0])
        clinton_deck.remove(clinton_deck[0])
        trump_deck.remove(trump_deck[0])
        print ("It is a Tie")
        print('_____________________________________________________________________________________\n\n\n')  


    rounds = rounds +1 #increament the round
    continue_game = "Y"
   
#End Game While Loop

#If Statments Declaring the Winner
if len(clinton_final_deck) > len(trump_final_deck):
    print ("Clinton WON!!!!")
    print ("Clinton cards won: " + str(len(clinton_final_deck)))
    print ("Trump  cards won: " + str(len(trump_final_deck)))
    print ("Tie Dump pile: " + str(len(tie_dump)))
if len(clinton_final_deck) < len(trump_final_deck):
    print ("Trump WON!!!!")
    print ("Clinton cards won: " + str(len(clinton_final_deck)))
    print ("Trump  cards won: " + str(len(trump_final_deck)))
    print ("Tie Dump pile: " + str(len(tie_dump)))
if len(clinton_final_deck)  ==  len(trump_final_deck):
    print ("It is a TIE!!!!")
    print ("Clinton cards won: " + str(len(clinton_final_deck)))
    print ("Trump  cards won: " + str(len(trump_final_deck)))
    print ("Tie Dump pile: " + str(len(tie_dump)))