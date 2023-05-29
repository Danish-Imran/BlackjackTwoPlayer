#!/usr/bin/env python
# Blackjack, created by Danish I.
# May 16, 2023

import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "J", "Q", "A",
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "J", "Q", "A",
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "J", "Q", "A",
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "J", "Q", "A"]

hand_one = []
hand_two = []
move_one = ""
move_two = ""

def sum_hand(hand): # calculates the sum of the cards in the player's hand
    sum = 0
    for card in hand:
        if isinstance(card, int) == True:
            sum += card
        if card == "K" or card == "J" or card == "Q":
            sum += 10
        if card == "A":
            if sum < 11:
                sum += 11
            else:
                sum += 1
    return sum

def draw_card(hand):
    card_chosen = random.choice(deck)
    hand.append(card_chosen)
    deck.remove(card_chosen)

# Give both players two cards

for i in range(2):
    card = random.choice(deck)
    hand_one.append(card)

for i in range(2):
    card = random.choice(deck)
    hand_two.append(card)

print(f"Player One has: {hand_one}")
print(f"Player Two has: {hand_two}")

# Begin game loop

while True: 
    if move_one.upper() != "S": # If they stood, skip their turn
        move_one = input("Player 1: [H]it or [S]tand? ")
        if move_one.upper() == "H":
            draw_card(hand_one)
            print(f"Player 1: {hand_one} ----- Total: {sum_hand(hand_one)}")
        else: # if they stand
            print(f"Player 1: {hand_one} ----- Total: {sum_hand(hand_one)}")
        if sum_hand(hand_one) > 21:
            break

    if move_two.upper() != "S": # If they stood, skip their turn
        move_two = input("Player 2: [H]it or [S]tand? ")
        if move_two.upper() == "H":
            draw_card(hand_two)
            print(f"Player 2: {hand_two} ----- Total: {sum_hand(hand_two)}")
        else: # if they stand
            print(f"Player 2: {hand_two} ----- Total: {sum_hand(hand_two)}")
        if sum_hand(hand_two) > 21:
            break
    if move_one.upper() == "S" and move_two.upper() == "S":
        break


# log results

print("")
if sum_hand(hand_one) > sum_hand(hand_two):
    print(f"Player 2 Total: {sum_hand(hand_two)}")
    print("Player Two is the winner!")
elif sum_hand(hand_two) > sum_hand(hand_one):
    print(f"Player 1 Total: {sum_hand(hand_one)}")
    print("Player One is the winner!")
else: # Tie
    print("It is a tie!")
