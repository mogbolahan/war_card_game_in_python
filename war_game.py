import random
import os
os.system('cls')
#Set Deck of cards AKA Main Deck
entire_deck_of_cards = ['QS', 'KS', 'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AH', '2H', '3H', '4H','AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS',  '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH']

#Shuffle the entire deck cards before game starts
random.shuffle(entire_deck_of_cards)

#Declare players decks before hand
Trump_deck = []
Clinton_deck = []

#Share the entire deck equally between the two players
while len(entire_deck_of_cards) !=0:
    Trump_deck.append(entire_deck_of_cards[0])
    entire_deck_of_cards.remove(entire_deck_of_cards[0])
    Clinton_deck.append(entire_deck_of_cards[0])
    entire_deck_of_cards.remove(entire_deck_of_cards[0])

#Declare variables
player_continue_loop = 'Y' #For Unless the player wants to end early
Trump_card_value = 0 #Worth of cards while fighting
Clinton_card_value = 0
Trump_final_deck = [] #Final list of the cards each player has at the end
Clinton_final_deck = []
tie_dump = [] #List cards lost by both contestant
rounds = 0 #Round counter

#Wait for user's input before proceeding with the game
player_continue_loop = input("Do you want to proceed? Enter Y/N?\n")

#While loop Starts Here
while len(Trump_deck) != 0 and len(Clinton_deck) != 0 and player_continue_loop != 'n' and player_continue_loop != 'N':

#Prints the stats of the game
    print ("Round: " + str(rounds))
    print ("Clinton Card: "+ Trump_deck[0])
    print ("Clinton Cards Left: "+str(len(Trump_deck)))
    print ("Clinton cards won: "+str(len(Trump_final_deck)) +"\n")
	
    print ("Trump's  Card: "+ Clinton_deck[0])
    print ("Trump's  Cards Left: "+str(len(Clinton_deck)))
    print ("Trump's  cards won: "+str(len(Clinton_final_deck)) +"\n")
	

#Rules to check the worth of each player's cards
    if len(Trump_deck) != 0:
        if Trump_deck[0][0] == 'A' and Clinton_deck[0][0] == 'K':
             Trump_card_value = 14
        elif Trump_deck[0][0] == 'A' and Clinton_deck[0][0] != 'K':
            Trump_card_value = 1
        elif Trump_deck[0][0] == 'T':
            Trump_card_value = 10
        elif Trump_deck[0][0] == 'J':
            Trump_card_value = 11
        elif Trump_deck[0][0] == 'Q':
            Trump_card_value = 12
        elif Trump_deck[0][0] == 'K':
            Trump_card_value = 13
        else:
            Trump_card_value = int(Trump_deck[0][0])
    if len(Clinton_deck) != 0:
        if Clinton_deck[0][0] == 'A' and Trump_deck[0][0] == 'K':
             Clinton_card_value = 14
        elif Clinton_deck[0][0] == 'A' and Trump_deck[0][0] != 'K':
            Clinton_card_value = 1
        elif Clinton_deck[0][0] == 'T':
            Clinton_card_value = 10
        elif Clinton_deck[0][0] == 'J':
            Clinton_card_value = 11
        elif Clinton_deck[0][0] == 'Q':
            Clinton_card_value = 12
        elif Clinton_deck[0][0] == 'K':
            Clinton_card_value = 13
        else:
            Clinton_card_value = int(Clinton_deck[0][0])

#Check the cards played by the two contestants to decide who won the round.
    if Trump_card_value > Clinton_card_value:
        Trump_final_deck.append(Clinton_deck[0])
        Clinton_deck.remove(Clinton_deck[0])
        Trump_final_deck.append(Trump_deck[0])
        Trump_deck.remove(Trump_deck[0])
        print ("Clinton is the winner of this round!")
    if Trump_card_value < Clinton_card_value:
        Clinton_final_deck.append(Trump_deck[0])
        Trump_deck.remove(Trump_deck[0])
        Clinton_final_deck.append(Clinton_deck[0])
        Clinton_deck.remove(Clinton_deck[0])
        print ("Trump's is the winner of this round!")
    if Trump_card_value == Clinton_card_value:
        tie_dump.append(Trump_deck[0])
        tie_dump.append(Clinton_deck[0])
        Trump_deck.remove(Trump_deck[0])
        Clinton_deck.remove(Clinton_deck[0])
        print ("The game is a tie!!!")

	#round Counter
    rounds = rounds +1 #increament the round
    player_continue_loop = "Y"
    print ("\n")

#while Loop Ends here

#Finally, announce the winner of the Election the Winner
if len(Trump_final_deck) > len(Clinton_final_deck):
    print ("Clinton WON!!!!")
    print ("Clinton's won cards: " + str(len(Trump_final_deck)))
    print ("Trump's won cards: " + str(len(Clinton_final_deck)))
    print ("Tie Dump pile: " + str(len(tie_dump)))
if len(Trump_final_deck) < len(Clinton_final_deck):
    print ("Trump HAS WON!!!!")
    print ("Clinton's won cards: " + str(len(Trump_final_deck)))
    print ("Trump's won cards: " + str(len(Clinton_final_deck)))
    print ("Tie Dump pile: " + str(len(tie_dump)))
if len(Trump_final_deck)  ==  len(Clinton_final_deck):
    print ("THE GAME IS A TIE!!!!")
    print ("Clinton cards won: " + str(len(Trump_final_deck)))
    print ("Trump's won cards: " + str(len(Clinton_final_deck)))
    print ("Tie Dump pile: " + str(len(tie_dump)))
