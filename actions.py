import random

def startOfTurn(userTurn, userScore, compScore):
    """
    At the start of turn, prints whose turn it is and the current score.
    :param userTurn: Bool that is True if it is the user's turn, false if it is computer's turn.
    :param userScore: Integer representing user's current score
    :param compScore: Integer representing computer's current score
    :return: None
    """

    if userTurn:
        print("\nIt's your turn!")
    else:
        print("It's my turn!")
    print(f"Your current score: {userScore}")
    print(f"My current score: {compScore}")


def showHand(userHand):
    """
    Tells the user what cards they have remaining in their hand
    :param userHand: list of cards representing the user's hand
    :return: None
    """
    print("\nYou have the following cards in your hand:")
    for card in userHand:
        print(f"{card["rank"]} of {card["suit"]}")

def validRank(userHand):
    """
    Get input from the user using the string passed to the function.
    Evaluate if this is a rank in the user's hand.
    :param userHand: user's hand
    :return: string representing valid rank the user has chosen.
    """
    rank = input("\nChoose a rank to fish for (ace, jack, king, queen, 2 to 10): ")
    return "ace"

def fishFromHand(rank, playerHand, userTurn):
    """
    This will "fish" through a hand of cards for any cards matching the rank given. If matching cards are found,
    they will be removed from the hand and returned as a list. If there are no matching cards, function will
    return an empty list. Will print a message about whether any cards were taken from the hand or whether to "Go fish".
    :param rank: String representing the rank of card to fish for.
    :param playerHand: The hand of cards to fish through.
    :param userTurn: Bool representing whether it is the user's turn.
    :return: A list of matching cards. Will be an empty list if no matching cards found.
    """
    print("Fishing from hand")
    print("No cards are found")
    return []

def goFish(rank, pond):
    """
    Will remove and return single random card from the pond.
    Will print a message for the user to let them know the results.
    :param rank: rank to search for
    :param pond: list of cards to draw from
    :return: card
    """
    print("Fishing from pond")
    card = [{'number': 'ace', 'suit': 'hearts'}]
    print(f"You got this card: {card}")
    return card


def compChoice(compHand):
    """
    Chooses a rank that the computer will fish for. Prints a message to the user.
    :param compHand: computer's hand of cards
    :return: string representing the rank to fish for.
    """
    print("Computer is choosing what to fish for")
    print("The computer chooses 'jack'.")
    return "jack"

def checkForBooks(userTurn, cardList):
    """
    Will go through the hand of cards given and look for any set of 4 cards with the same rank. If any sets of four,
    or "books" are found, these cards will be removed from the hand. Print a message if any books are found.
    Function will return the number of books found.
    :param userTurn: bool representing whether it is the user's turn
    :param cardList: list of cards to search through for sets of 4
    :return: an integer representing the number of books found
    """
    print("Checking for 'books'.")
    print("No books found.")
    return 0

def checkForEndgame(userScore, compScore, userHand, compHand, pond):
    """
    Will check whether any end game conditions have been met. Returns True if they have, False otherwise.
    Will print a message about what triggered the end of the game.
    :param userScore: integer representing the user's score
    :param compScore: integer representing the computer's score
    :param userHand: list of cards representing the user's hand
    :param compHand: list of cards representing the computer's hand
    :param pond: list of cards representing the pond
    :return: True if any endgame conditions are met. False if not.
    """
    print("Checking for endgame conditions.")
    print("No endgame conditions found.")
    return False


def displayGameResults(userScore, compScore):
    """
    Will print the user's and computer's scores and print a message about who won.
    :param userScore: integer representing the user's score
    :param compScore: integer representing the computer's score
    :return: None
    """
    print("Displaying computer score")
    print("Displaying player score")
    print("Printing a message about who won.")

def continuePlaying():
    """
    Asks the user if they want to play another round of Go Fish
    :return: True if user wants to play another round. False to stop playing.
    """
    print("Asking if user wants to play another round.")
    print("The user says yes")
    return True