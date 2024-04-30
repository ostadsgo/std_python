# -----------------
# Guessing Game
# ----------------
import random

print("That is a test.")
rand_number = random.randrange(1, 100)
is_win = False

print("I am number between 1 to 99")
print("Try to guess me.")

print(rand_number)

for i in range(10):
    user_guess = int(input("Your guess > "))

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
