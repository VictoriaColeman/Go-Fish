# ------------------------------------------------------------------------
#
#  Program: Go Fish
#
#  Description: This program allows you to play a two-person game of Go
#  Fish against the computer.
#
#  Author: Victoria Coleman
#  Created: March 10, 2026
#
# ------------------------------------------------------------------------

from actions import *
from deck import DECK, dealHand
from instructions import gameInstructions

def main():
    #Print game instructions and ask user if they want to play.
    playing = printInstructions(gameInstructions)

    #User will always be the first player
    userTurn = True

    while playing:

        #This creates the pond of cards that can be drawn from. This is the deck that can be altered as the game is played.
        pond = list(DECK)

        #Deal a starting hand to the user and then to the computer.
        userHand = dealHand(7, pond)
        compHand = dealHand(7, pond)

        #Set scores to zero
        userScore = 0
        compScore = 0

        #User and computer will continue taking turns until endgame conditions are met.
        gameOver = False
        while not gameOver:
            #Print out whose turn it is and current scores.
            startOfTurn(userTurn, userScore, compScore)

            #Check whose turn it is and determine which rank to fish for
            if userTurn:
                playerHand = userHand
                opponentHand = compHand
                showHand(userHand)
                print(compHand) #HERE FOR TESTING ONLY
                rank = validRank(userHand)
            else:
                playerHand = compHand
                opponentHand = userHand
                rank = compChoice(compHand)

            #Take any matching cards from the other player's hand
            cardsTaken = fishFromHand(rank, opponentHand, userTurn)

            #If any cards are taken, add to player's hand. Else, go fish
            if cardsTaken:
                playerHand += cardsTaken
            else:
                card = goFish(pond, userTurn)
                pond.remove(card)
                playerHand.append(card)

            #Search for sets of 4 matching cards and update the score
            pointsGained = checkForBooks(userTurn, playerHand)
            if userTurn:
                userScore += pointsGained
            else:
                compScore += pointsGained

            #Check whether any endgame conditions have been met
            gameOver = checkForEndgame(userScore, compScore, userHand, compHand, pond)

            #Switch active player - will flip the boolean value of the variable
            userTurn = not userTurn

        #If endgame conditions have been met, print score and who won
        displayGameResults(userScore, compScore)

        #Check if the user wants to play another round.
        if continuePlaying():
            print("Great! Let's start another round of Go Fish!")
        else:
            playing = False


if __name__ == "__main__":
    main()





