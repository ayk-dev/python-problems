import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    # 0 represents Blackjack, score of 21 with 2 cards only
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare_score(user, computer):
    if user > 21 and computer > 21:
        return "You lose"

    if user == computer:
        return "Draw"

    if computer == 0:
        return "You lose, opponent has Blackjack"
    if user == 0:
        return "You win with a Blackjack"

    if user > 21:
        return "You went over. You lose"
    if computer > 21:
        return "Opponent went over. You win"
    if user > computer:
        return "You win"
    else:
        return "You lose"