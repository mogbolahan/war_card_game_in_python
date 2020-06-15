import random
from time import localtime,strftime

# import only system from os 
from os import system, name 


#declare and assign global variables
continue_game = 'Y' #For Unless the player wants to end early
clinton_card_value = 0 #Worth of cards while fighting
trump_card_value = 0
clinton_final_deck = [] #Final list of the cards each player has at the end
trump_final_deck = []
ties = [] #List cards lost by both contestant


# define our clear screen function 
def clear_screen(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


def print_intro():
  tme = localtime();
  timeString = strftime("%m/%d/%y %H:%M:%S", tme);
  
  print("\n###########################################################################################################################")
  print("#	Python implementation of the popular card war game.")
  print("#       War is a card game, typically played by two players using a standard playing card deck[2] — and often played by children.")
  print("#	The deck is divided evenly among the players, giving each a down stack.") 
  print("#       In unison, each player reveals the top card of their deck—this is a battle —and" )
  print("#	The player with the higher card takes both of the cards played and moves them to their stack.")
  print("#       Aces are high, and suits are ignored.")
  print("#       Reference: https://en.wikipedia.org/wiki/War_(card_game)                                ")
  print("#       This software and associated documentation (if any) is furnished under a MIT license (See my github repo for details).")
  print("#       Mogbolahan Ojeyinka. Copyright (c) 2020 All rights reserved. ")
  print("#	" + timeString												 					  )
  print("#############################################################################################################################\n")
  
def play_game():
    #assign card list
    entire_deck_of_cards = ['QS', 'KS', 'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AH', '2H', '3H', '4H','AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS',  '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH']
    
    #shuffle the entire deck cards before game starts
    random.shuffle(entire_deck_of_cards)
    
    #Declare players decks before hand
    clinton_deck = []
    trump_deck = []

    #share the entire deck equally between the two players
    while len(entire_deck_of_cards) !=0:
        clinton_deck.append(entire_deck_of_cards[0])
        entire_deck_of_cards.remove(entire_deck_of_cards[0])
        trump_deck.append(entire_deck_of_cards[0])
        entire_deck_of_cards.remove(entire_deck_of_cards[0])
    
    rounds = 0 #Round counter
    
    #wait for user's input before proceeding with the game
    print("The names of the players are Clinton and Trump.\n")
    continue_game = input("Do you want to proceed? Enter Y/N? ")
    
    #while loop starts here
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
            ties.append(clinton_deck[0])
            ties.append(trump_deck[0])
            clinton_deck.remove(clinton_deck[0])
            trump_deck.remove(trump_deck[0])
            print ("It is a Tie")
            print('_____________________________________________________________________________________\n\n\n')  
    
    
        rounds = rounds +1 #increament the round
        continue_game = "Y"
   
#End of while Loop
def print_game_summary():
    print('################################### SUMMARY ##########################################')
    print('######################################################################################')
    print ("                            "  + "Cards won                                                #")
    print('-------------------------------------------------------------------------------------#')
    print ('{0: <30}'.format("Clinton") +  '{0: <55}'.format(str(len(clinton_final_deck))) + "#")
    print ('{0: <30}'.format("Trump") +  '{0: <55}'.format(str(len(trump_final_deck))) + "#")
    print ('{0: <30}'.format("No of ties") +  '{0: <55}'.format(str(len(ties))) + "#")
    print('######################################################################################')
    
#Declare the winner
def declare_winner():
    print ('{0: <85}'.format(" ")+"#")
    print ('{0: <85}'.format(" ")+"#")
    if len(clinton_final_deck) > len(trump_final_deck):
        print ('{0: <20}'.format("") + "CLINTON WON THE GAME" +  '{0: <45}'.format("") + "#")
    if len(clinton_final_deck) < len(trump_final_deck):
        print ('{0: <20}'.format("") + "TRUMP WON THE GAME" +  '{0: <47}'.format("") + "#")
    if len(clinton_final_deck)  ==  len(trump_final_deck):
        print ('{0: <20}'.format("") + "THE GAME IS A TIE" +  '{0: <48}'.format("") + "#")
    print ('{0: <85}'.format(" ")+"#")
    print ('{0: <85}'.format(" ")+"#")
    print('######################################################################################')
      
      

	
## Main Block ##
clear_screen() # call clear_screen function defined above 
print_intro()
play_game()
print_game_summary()
declare_winner()