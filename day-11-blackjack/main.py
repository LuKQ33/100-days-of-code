import random

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    card = random.choice(cards)
    return card


def calculate_score(card_list):
    score = sum(card_list)
    if len(card_list) == 2 and score == 21:
        return 0
    if score > 21 and 11 in card_list:
        score -= 10
        card_list.remove(11)
        card_list.append(1)
        return score
    return score


