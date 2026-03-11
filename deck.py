import random

#This is how I built the 52-card standard deck so that I did not have to type out each card.
ranks = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
suits = ["hearts", "spades", "clubs", "diamonds"]
def buildDeck():
    deck = ()
    for suit in suits:
        for rank in ranks:
            deck += ({"rank": rank, "suit": suit},)
    return deck

#This is a tuple representing a standard 52-card deck. It is a tuple so that it is never altered.
DECK = buildDeck()

def dealHand(numCards, cardList):
    """
    Draws a hand of cards from a deck and returns a list of cards. Does alter the deck to remove the cards drawn.
    :param numCards: Number of cards to draw
    :param cardList: A list that contains the cards that can be drawn. Is altered by the function.
    :return: Returns a list of cards drawn.
    """
    hand = []
    for each in range(numCards):
        card = random.choice(cardList)
        cardList.remove(card)
        hand.append(card)
    return hand

