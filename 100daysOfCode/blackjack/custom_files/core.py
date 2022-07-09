from logo import logo
from custom_files.helper import deal_card, calculate_score, compare_score


def play_blackjack():
    print(logo)

    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    while not game_over:
        print()
        print(f'   Your cards: {user_cards}, current score: {user_score}')
        print(f'   Computer\'s first card: {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print()
    print(f'Your final hand: {user_cards}, final score: {user_score}')
    print(f'Computer\'s final hand: {computer_cards}, final score: {computer_score}')
    print()
    print(compare_score(user_score, computer_score))
    print()