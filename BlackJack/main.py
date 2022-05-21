from card import *
from deck import *
from bjhand import *
from hand import *
from handTests import *


def main():
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
    # testHasCardWithValue()
    # print()
    # testHasCardWithSuit()
    # print()
    # testIndexOf()
    # print()
    # testScore()
    # print()
    # testIsAce()
    # print()
    print("Welcome to Blackjack\n")
    print("Play Blackjack against the dealer")
    deck = Deck()  # create deck
    deck.shuffle()  # shuffle deck

    playerHand = BJHand()  # create bj hand
    playerHand.addCard(deck.deal())  # add card from deck to hand
    playerHand.addCard(deck.deal())
    print()
    dealerHand = BJHand()
    dealerHand.addCard(deck.deal())
    dealerHand.addCard(deck.deal())
    print(f"Player's {playerHand}Player's Score: {playerHand.score}\n")  # show players hand and score
    print(f"Dealer's {dealerHand[1]}")  # shows 2nd card from dealers hand
    hit = input("Do you want to hit or stand? Type hit/stand: ")  # ask if user wants another card

    while hit == "hit":
        playerHand.addCard(deck.deal())  # add card from deck to player hand
        print(f"Player's {playerHand}Player's score: {playerHand.score}\n")
        hit = input("Do you want to hit or stand? Type hit/stand: ")  # ask again
        if hit == "hit":
            dealerHand.addCard(deck.deal())  # if yes, add another card

    if playerHand.isBusted():  # if player score is over 21, bust
        print("You busted. The dealer wins!")
    else:
        print()
        print(f"Dealer's {dealerHand}")  # display dealers hand
        while dealerHand.score <= 16:  # if dealers hand < 17
            dealtCard = deck.deal()  # deal card
            print(f"Dealer has dealt: {dealtCard}")  # show dealt card
            dealerHand.addCard(dealtCard)  # add card to dealers hand
            print(f"Dealer's {dealerHand}Dealer's score: {dealerHand.score}\n")  # display dealers score

        if dealerHand.isBusted():  # bust if dealers hand is > 21
            print(f"Dealer's score: {dealerHand.score}")
            print("The dealer busted. You win!")
        elif playerHand.score > dealerHand.score:  # player wins if score > dealer
            print(f"Dealer's score: {dealerHand.score}")
            print("You win!")
        elif playerHand.score < dealerHand.score:  # dealer wins if score > player
            print("The dealer wins")
        else:
            print("It's a tie.")





if __name__ == '__main__':
    main()
