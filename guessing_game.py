# -----------------
# Guessing Game
# ----------------
from random import randrange


def intro_message():
    print("I am number between 1 to 99")
    print("Try to guess me.")


def get_user_guess():
    user_guess = None
    try:
        user_guess = int(input("Your guess > "))
    except ValueError:
        print("The value is not a number.")
    return user_guess


def compare(user_guess, rand_number):
    try:
        if user_guess > rand_number:
            return 1
        elif user_guess < rand_number:
            return -1
        else:
            return 0
    except TypeError:
        print(f"The value `{user_guess}` is invalid")


rand_number = randrange(1, 100)
is_win = False

intro_message()


for i in range(10):
    user_guess = get_user_guess()
    if user_guess == None:
        continue

    result = compare(user_guess, rand_number)
    if result == 0:
        is_win = True
        print(f"You win in {i} times.")
        break
    elif result == -1:
        print("Try higher")
    else:
        print("Try lower.")


# if the user didn't win.
if is_win == False:
    print("You didn't win.")
