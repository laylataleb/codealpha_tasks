import random
from  wordlist import  word_list
from colorama import Fore,init 

init(autoreset=True)
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def select_random_word(word_list):
    return random.choice(word_list)

def display_man(incorrect_guesses):
    print(Fore.LIGHTBLUE_EX+"##########")
    for line in hangman_art[incorrect_guesses]:
        print(line)
    print(Fore.LIGHTBLUE_EX+"##########")


def display_progress(word, guessed_letters):
    progress = ""
    for letter in word:
        if letter==" ":
            progress +="  "
        elif letter in guessed_letters:
            progress += Fore.YELLOW + letter 
        else:
            progress += Fore.BLUE + "_ "  
    return progress

def get_player_input(guessed_letters):
    while True:
        guessed_letter = input("Guess a letter: ").lower()

        if len(guessed_letter) != 1:
            print(Fore.YELLOW + "Please enter a single alphabetic character.")
            continue
        
        if  not guessed_letter.isalpha():
            print(Fore.CYAN +"Please enter an alphabetic character. ")
            continue

        if guessed_letter in guessed_letters:
            print(Fore.LIGHTMAGENTA_EX + "You've already guessed that letter. Try another one.")
            continue

        return guessed_letter

def play_hangman():
    selected_word = select_random_word(word_list)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    while incorrect_guesses < max_incorrect_guesses:
        display_man(incorrect_guesses)
        print("Hint: Flowers")
        print(f"Current progress: {display_progress(selected_word, guessed_letters)}")
        guessed_letter = get_player_input(guessed_letters)

        guessed_letters.append(guessed_letter)

        if guessed_letter not in selected_word:
            incorrect_guesses += 1
           # print(f"Incorrect! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        if "_" not in display_progress(selected_word, guessed_letters):
            print(Fore.GREEN + f"     Congratulations! The word is: {selected_word}")
            break
    else:
        print(Fore.RED + f"Game over! The word was: {selected_word}")

if __name__ == "__main__":
    play_hangman()
