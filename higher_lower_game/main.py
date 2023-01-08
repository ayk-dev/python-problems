import random

from art import logo, vs
from game_data import data


def get_random_data():
    return random.choice(data)


def play_game():
    score = 0

    comp_a = get_random_data()
    print(f'Compare A: {comp_a["name"]}, a {comp_a["description"]}, from {comp_a["country"]}.')
    print(vs)
    comp_b = get_random_data()
    print(f'Against B: {comp_b["name"]}, a {comp_b["description"]}, from {comp_b["country"]}.')
    result = 'a' if comp_a["follower_count"] > comp_b["follower_count"] else 'b'
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    while guess == result:
        score += 1
        print(f"You're right! Current score: {score}.")
        print()
        comp_a = comp_b
        comp_b = get_random_data()
        print(f'Compare A: {comp_a["name"]}, a {comp_a["description"]}, from {comp_a["country"]}.')
        print(vs)
        print(f'Against B: {comp_b["name"]}, a {comp_b["description"]}, from {comp_b["country"]}.')
        result = 'a' if comp_a["follower_count"] > comp_b["follower_count"] else 'b'
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print(f"Sorry, that's wrong. Final score: {score}")


print(logo)

play_game()


