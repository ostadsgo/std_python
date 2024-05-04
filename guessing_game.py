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


rand_number = randrange(1, 100)
is_win = False

intro_message()


for i in range(10):
    user_guess = get_user_guess()
    if user_guess == None:
        continue

    # Compare user input with random number.
    if user_guess > rand_number:
        print("Try lower.")
    elif user_guess < rand_number:
        print("Try higher")
    else:
        print("You win.")
        is_win = True
        break

# if the user didn't win.
if is_win == False:
    print("You didn't win.")
