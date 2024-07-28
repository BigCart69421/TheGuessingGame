import random


def number_guessing_game():
    attempts = int(input("How many attempts do you want: "))
    max_number = int(input("Choose your max number: "))

    print("Welcome to BigCart's Guessing Game!")
    print(f"You have {attempts} attempts to guess a number between 1 and {max_number}.")

    random_number = random.randint(1, max_number)  # Generate the random number once

    while attempts > 0:
        guess = int(input("Guess a number: "))

        if guess == random_number:
            print("Congratulations! You guessed correctly!")
            break
        else:
            attempts -= 1
            if guess < random_number:
                print("Too low!")
            else:
                print("Too high!")

            print(f"You have {attempts} attempts left.")

    if attempts == 0:
        print(f"Sorry, you ran out of attempts. The number was {random_number}")

# Main game loop
while True:
    number_guessing_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break


