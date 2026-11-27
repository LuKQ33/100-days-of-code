import random

import art

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Deals a random card from list and returns it"""
    card = random.choice(CARDS)
    return card


def calculate_score(card_list):
    """Returns the sum of the card list and evaluates Blackjack or +21"""
    score = sum(card_list)
    if len(card_list) == 2 and score == 21:
        return 0
    while score > 21 and 11 in card_list:
        score -= 10
        card_list.remove(11)
        card_list.append(1)
    return score


def compare_scores(user_score, computer_score):
    """Compare the scores and returns the result"""
    if user_score == computer_score:
        return "Draw"
    if computer_score == 0:
        return "Lose, opponent has Blackjack."
    if user_score == 0:
        return "Win with a Blackjack."
    if user_score > 21:
        return "You went over. You lose."
    if computer_score > 21:
        return "Opponent went over. You win"
    if user_score > computer_score:
        return "You win."
    else:
        return "You lose."


def play_game():
    """Runs a complete round of Blackjack between the player and the dealer."""
    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"Player hand {player_cards}. Current score: {player_score}")
    print(f"Dealer hand [{dealer_cards[0]}, X]")
    if player_score == 0:
        print(f"Player hand {player_cards}. Current score: {player_score}")
        print(compare_scores(player_score, dealer_score))
    elif dealer_score == 0:
        print(f"Dealer hand {dealer_cards} scores {dealer_score}")
        print(compare_scores(player_score, dealer_score))
    else:
        is_game_over = False
        while not is_game_over:
            get_another_card = input("\nType 'y' to get another card"
                                     ", type 'n' to pass: ")
            if get_another_card == 'y':
                player_cards.append(deal_card())
                player_score = calculate_score(player_cards)
                print(f"Player hand {player_cards}. Current score: {player_score}")
                if player_score > 21:
                    print(compare_scores(player_score, dealer_score))
                    is_game_over = True
            elif get_another_card == 'n':
                while dealer_score < 17:
                    # dealer draws cards until it scores at least 17
                    dealer_cards.append(deal_card())
                    dealer_score = calculate_score(dealer_cards)
                    print(f"Dealer hand {dealer_cards} scores {dealer_score}")
                print(f"\nYour final hand: {player_cards}, final score: {player_score}")
                print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
                print(compare_scores(player_score, dealer_score))
                is_game_over = True


keep_playing = True

while keep_playing:
    choice = input("\nDo you want to play a game of BlackJack? Type 'y' or 'n': ")
    if choice == 'y':
        print(art.logo)
        play_game()
    elif choice == 'n':
        print("\nBye bye!")
        keep_playing = False
