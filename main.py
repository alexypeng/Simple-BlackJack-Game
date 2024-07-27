# Simple BlackJack game programmed by Alexander Peng

from replit import clear
from art import logo
import random

CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def winner(player_hand, computer_hand):
    """Checks the winner between the player and the computer"""

    print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
    print(
        f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}"
    )

    if sum(player_hand) > 21:
        print("You went over. You lose.")
    elif sum(computer_hand) > 21:
        print("Opponent went over. You win!")
    elif sum(player_hand) > sum(computer_hand):
        print("You win!")
    elif sum(player_hand) == sum(computer_hand):
        print("Draw.")
    else:
        print("You lose.")


def draw_card(hand):
    """Adds a card to [hand] and returns the updated [hand]"""

    hand.append(CARDS[random.randint(0, 11)])
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)

    return hand


def game():
    """BlackJack game"""

    play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    while play != "n":
        clear()

        win = True
        player_hand = []
        computer_hand = []

        player_hand = draw_card(player_hand)
        player_hand = draw_card(player_hand)
        computer_hand = draw_card(computer_hand)

        print(logo)
        print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
        print(f"Computer's first card: {computer_hand[0]}")

        draw = input("Do you want to draw a card? ")

        while draw.lower() == "y" and win:
            player_hand = draw_card(player_hand)
            print(
                f"Your cards: {player_hand}, current score: {sum(player_hand)}"
            )
            print(f"Computer's first card: {computer_hand[0]}")

            if sum(player_hand) > 21:
                win = False
            else:
                draw = input("Do you want to draw a card? ")

        while sum(computer_hand) < 17 and win:
            computer_hand = draw_card(computer_hand)

        winner(player_hand, computer_hand)

        play = input(
            "Do you want to play a game of BlackJack? Type 'y' or 'n': ")


game()
