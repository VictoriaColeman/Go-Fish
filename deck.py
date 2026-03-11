

def buildDeck():
    """
    Creates a tuple representing a standard 52-card deck where each card is a dictionary with a rank and suit.
    :return: tuple representing the deck
    """
    ranks = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
    suits = ["hearts", "spades", "clubs", "diamonds"]
    deck = ()
    for suit in suits:
        for rank in ranks:
            deck += ({"rank": rank, "suit": suit},)
    return deck

DECK = buildDeck()

