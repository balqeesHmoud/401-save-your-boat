import random

# Welcome message and game description
def print_welcome_message():
    desc1 = "1) You have a boat that has 5 lives and it will drown."
    desc2 = "2) Guess the word by choosing one letter at a time from the English alphabet."
    desc3 = "3) Incorrect guesses will cost you a life."
    desc4 = "4) Correct guesses will reveal the letters in the word."
    desc5 = "5) Guess the entire word correctly to save your boat and win!"
    desc6 = "6) Use 'exit' to quit the game anytime."
    
    print("Welcome To Save Boat Game :D\n\nDescription:\n")
    print(desc1)
    print(desc2)
    print(desc3)
    print(desc4)
    print(desc5)
    print(desc6)


# Function to give hints based on the number of hints already given
def give_hint(hints_given):
    hints = ["food", "Maybe red, green, yellow", "It starts with the letter 'a'"]
    if hints_given < len(hints):
        print("Hint:", hints[hints_given])
    else:
        print("No more hints available!")


# Function to play the game
def save_your_boat():
    hints_given = 0
    word_to_guess = random.choice(["apple", "orange", "banana", "lemon", "mango"])
    word_display = "_" * len(word_to_guess)
    lives = 5

    print_welcome_message()
    answer = input("\n\nWanna play? (y/n): ").lower()

    if answer != 'y':
        print("Maybe next time!")
        return

    print("Let's play the game!\n")

    while lives > 0:
        print("Word to guess:", " ".join(word_display))
        print("Boat lives:", lives)

        guess = input("Choose a letter: ").lower()

        if guess == "exit":
            print("Exiting the game.")
            break

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in word_to_guess:
            print("Yay! You got it right.")
            updated_word_display = ""
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    updated_word_display += guess
                else:
                    updated_word_display += word_display[i]
            word_display = updated_word_display
        else:
            lives -= 1
            print("You got it wrong.")
            give_hint(hints_given)
            hints_given += 1

        if "_" not in word_display:
            print("Congratulations! You guessed the word:", word_to_guess)
            print("You Win!")
            break

        if lives == 1 and hints_given < 3:
            give_hint(hints_given)

    if lives == 0:
        print("Game Over! You ran out of lives. The word was:", word_to_guess)


# Entry point of the program
if __name__ == "__main__":
    save_your_boat()
