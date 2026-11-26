import random

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    card = random.choice(cards)
    return card


def calculate_score(card_list):
    score = sum(card_list)
    return score


player_cards = [
    deal_card(), deal_card()
]

print(player_cards)

dealer_cards = [
    deal_card(), deal_card()
]

print(dealer_cards)


print(calculate_score(player_cards))