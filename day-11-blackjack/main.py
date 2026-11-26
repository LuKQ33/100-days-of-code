import random

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Deals a random card from list and returns it"""
    card = random.choice(cards)
    return card


def calculate_score(card_list):
    """Returns the sum of the card list and evaluates Blackjack or +21"""
    score = sum(card_list)
    if len(card_list) == 2 and score == 21:
        return 0
    if score > 21 and 11 in card_list:
        score -= 10
        card_list.remove(11)
        card_list.append(1)
        return score
    return score



keep_playing = True

while keep_playing:
    choice = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    if choice == 'y':
        player_cards = [deal_card(), deal_card()]
        dealer_cards = [deal_card(), deal_card()]
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(art.logo)
        print(f"Player hand {player_cards}. Current score: {player_score}")
        print(f"Dealer hand [{dealer_cards[0]}, X]")
        if player_score == 0:
            print("BlackJack! You win")
        elif dealer_score == 0:
            print("Dealer has BlackJack. You lose")
        else:
            while True:
                get_another_card = input("Type 'y' to get another card"
                                         ", type 'n' to pass: ")
                if get_another_card == 'y':
                    player_cards.append(deal_card())
                    player_score = calculate_score(player_cards)
                    print(f"Player hand {player_cards}. Current score: {player_score}")
                    if player_score > 21:
                        print("You lose!")
                        break
                elif get_another_card == 'n':
                    while dealer_score < 17:
                        dealer_cards.append(deal_card())
                        dealer_score = calculate_score(dealer_cards)
                        print(f"Dealer hand {dealer_cards} scores {dealer_score}")
                    if dealer_score > 21:
                        print("You win!")
                        break
                    if player_score > dealer_score:
                        print(f"Dealer hand {dealer_cards}")
                        print("You win!")
                        break
                    elif player_score == dealer_score:
                        print(f"Dealer hand {dealer_cards}")
                        print("Tie.")
                        break
                    else:
                        print(f"Dealer hand {dealer_cards}")
                        print(f"Dealer wins with {dealer_score}")
                        break
    elif choice == 'n':
        print("Bye bye!")
        keep_playing = False








