from card import *
from deck import *
from bjhand import *
from handTests import *
from hand import *


def main():
<<<<<<< HEAD
    while True:
        print("Welcome to Blackjack\n")
        deck = Deck()
        deck.shuffle()

        playerHand = BJHand()
        playerHand.addCard(deck)
        playerHand.addCard(deck)

        dealerHand = BJHand()
        dealerHand.addCard(deck)
        dealerHand.addCard(deck)
        print(f"Player score: {playerHand.theScore()}")

=======

    # testConstructor()
    # print()
    # testAddCard()
    # print()
    # testDisCard()
    # print()
    # testGetItem()
    # print()
    # testHasCard()
    # print()
    # testIndexOf()
    # print()
    # testHasCardWithValue()
    # print()
    # testHasCardWithSuit()
    # print()

    testConstructor()
    print()
    testAddCard()
    print()
    testDisCard()
    print()
    testGetItem()
    print()
    testHasCard()
    print()
    # testIndexOf()
    print()
    testHasCardWithValue()
    print()
    testHasCardWithSuit()
>>>>>>> 2ed36f2732b8eb76580e3f153fecc9c902458bb0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
