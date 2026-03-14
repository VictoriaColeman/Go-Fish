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
from deck import DECK
from instructions import gameInstructions

def main():
    #Print game instructions and ask user if they want to play.
    playing = printInstructions(gameInstructions)

    while playing: #Each loop is a GAME of GO Fish
        # User will always be the first player
        userTurn = True

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
        #This flag will be used to determine if a loop is a continuation of player turn
        #(because they got what they asked for)
        keepFishing = False

        while not gameOver:
            #Print out whose turn it is and current scores.
            if not keepFishing:
                startOfTurn(userTurn, userScore, compScore)  # only print start of turn message if we switched players
            else:
                if userTurn:
                    print("\nYou got what you asked for. You get to go again!")
                else:
                    print("\nYour opponent got what they asked for. They get to go again!")

            #Check whose turn it is and determine which rank to fish for
            if userTurn:
                playerHand = userHand
                opponentHand = compHand
                showHand(userHand)
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
                keepFishing = True
            else:
                card = goFish(pond, userTurn)
                pond.remove(card)
                playerHand.append(card)
                if card["rank"] == rank:
                    keepFishing = True
                else:
                    keepFishing = False

            #Search for sets of 4 matching cards and update the score
            pointsGained = checkForBooks(userTurn, playerHand)
            if userTurn:
                userScore += pointsGained
            else:
                compScore += pointsGained

            #Check whether any endgame conditions have been met
            gameOver = checkForEndgame(userScore, compScore, userHand, compHand, pond)

            #Switch active player if fishing unsuccessful
            if not keepFishing:
                userTurn = not userTurn

        #If endgame conditions have been met, print score and who won
        displayGameResults(userScore, compScore)

        #Check if the user wants to play another round.
        if continuePlaying():
            print("Great! Here we go!")
        else:
            playing = False


if __name__ == "__main__":
    main()





