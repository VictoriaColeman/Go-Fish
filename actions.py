import random

def printInstructions(instructions):
    """
    Print game instructions, then ask user if they want to play. Validate user response.
    :param instructions: string containing Go Fish game instructions
    :return: bool that is True if the user wants to play, False to exit
    """
    print(instructions)
    response = input("\nAre you ready to play Go Fish? (y/n) ").lower()
    while response not in ["y", "n"]:
        response = input("Invalid response. Please type 'y' to play or 'n' to exit: ").lower()
    return response == "y"


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
        print("\nIt's the computer's turn!")
    print(f"Your current score: {userScore}")
    print(f"Computer's current score: {compScore}")


def showHand(userHand):
    """
    Tells the user what cards they currently have in their hand.
    :param userHand: list of cards representing the user's hand
    :return: None
    """
    print("\nYou have the following cards in your hand:")
    for card in userHand:
        print(f"{card["rank"]} of {card["suit"]}")

def validRank(userHand):
    """
    Ask the user what rank they want to fish for and validate their response.
    Response must be a valid rank that the user has in their hand.
    :param userHand: user's hand
    :return: string representing valid rank the user has chosen.
    """
    ranksInHand = []
    for card in userHand:
        ranksInHand.append(card["rank"])
    rank = input("\nChoose a rank to ask for (ace, jack, king, queen, 2 to 10): ").lower()
    while rank not in ranksInHand:
        rank = input("Invalid response. Please choose a rank that you have in your hand: ").lower()
    print(f"\nYou say: Give me your {rank}'s.")
    return rank

def fishFromHand(rank, playerHand, userTurn):
    """
    This will "fish" through a hand of cards for any cards matching the rank given. If matching cards are found,
    they will be removed from the hand and returned as a list. If there are no matching cards, function will
    return an empty list. Will print a message about whether any cards were taken from the hand or whether to "Go fish".
    :param rank: String representing the rank of card to fish for.
    :param playerHand: A list representing the hand of cards to fish through.
    :param userTurn: Bool representing whether it is the user's turn.
    :return: A list of matching cards. Will be an empty list if no matching cards found.
    """
    cardsTaken = []
    for card in playerHand:
        if card["rank"] == rank:
            cardsTaken.append(card)
    for card in cardsTaken:
        playerHand.remove(card)
    if userTurn:
        player = "You"
        opponent = "The computer"
        verb = "says"
    else:
        player = "The computer"
        opponent = "You"
        verb = "say"
    if cardsTaken:
        print(f"\n{player} took the following card(s):")
        for card in cardsTaken:
            print(f"{card["rank"]} of {card["suit"]}")
    else:
        print(f"\n{opponent} {verb}: Go fish!")
    return cardsTaken


def goFish(pond, userTurn):
    """
    Returns a single random card from the pond.
    Prints a message for the user to let them know the results.
    :param pond: list of cards to draw from
    :param userTurn: bool representing whether it is the user's turn
    :return: dictionary representing a single card
    """
    card = random.choice(pond)
    if userTurn:
        print(f"\nYou took this card from the pond: \n{card["rank"]} of {card["suit"]}")
    else:
        print("\nThe computer took a card from the pond.")
    return card


def compChoice(compHand):
    """
    Chooses a rank that the computer will fish for. Prints a message to the user.
    :param compHand: computer's hand of cards
    :return: string representing the rank to fish for.
    """
    ranksInHand = []
    for card in compHand:
        ranksInHand.append(card["rank"])
    choice = random.choice(ranksInHand)
    print(f"\nThe computer says: Give me your {choice}'s.")
    return choice

def checkForBooks(userTurn, playerHand):
    """
    Will go through the hand of cards given and look for any set of 4 cards with the same rank. If any sets of four,
    or "books" are found, these cards will be removed from the hand. Print a message if any books are found.
    Function will return the number of books found.
    :param userTurn: bool representing whether it is the user's turn
    :param playerHand: list of cards to search through for sets of 4
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
    if userScore + compScore == 13:
        print("\nAll 13 sets of 4 have been collected!")
    elif not userHand:
        print("\nYou are out of cards!")
    elif not compHand:
        print("\nThe computer is out of cards!")
    elif not pond:
        print("\nThere are no cards left in the pond!")
    else:
        return False
    print("Game over. Let's see who won.")
    return True


def displayGameResults(userScore, compScore):
    """
    Will print the user's and computer's scores and print a message about who won.
    :param userScore: integer representing the user's score
    :param compScore: integer representing the computer's score
    :return: None
    """
    print(f"\nYour score: {userScore}")
    print(f"The computer's score: {compScore}")
    if userScore > compScore:
        print("You win!")
    elif compScore > userScore:
        print("The computer wins.")
    else:
        print("It's a tie!")

def continuePlaying():
    """
    Asks the user if they want to play another round of Go Fish
    :return: True if user wants to play another round. False to stop playing.
    """
    answer = input("\nDo you want to play another round of Go Fish? (y/n) ").lower()
    while answer not in ['y', 'n']:
        answer = input("Invalid response. Please type 'y' to play another round, 'n' to exit. ").lower()
    return answer == 'y'