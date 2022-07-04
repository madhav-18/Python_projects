import random
from game_data import data

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


def format_data(account):
    """Format the data that we want to print about the that person."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f"{name}, a {description}, from {country}")
    return f"{name}, a {description}, from {country}"


def get_random_account():
    """gets random data from the list"""
    return random.choice(data)


def check_answer(guess, a_followers, b_followers):
    """check if followers that the user guessed and return True if they guessed right and False if they guessed wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    """gets a random account"""
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")

        guess = input("Who has more followers. Type 'A' or 'B': ")
        a_followers_count = account_a["follower_count"]
        b_followers_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_followers_count, b_followers_count)

        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()