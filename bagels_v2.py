from random import shuffle
import sys

GUESS_DIGITS = 3
NUM_GUESSES = 10

def main():
    print("""Bagels, a deductive logic game.
By Akeem Mudashiru akeemmudash@gmail.com
          
I am thinking of a {}-digit number. Try to guess what it is.
Here are some clues:
When I say:     That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is incorrect and in the right position.
    Bagels      No digit is correct.
I have thought up a number.
    You have 10 guesses to get it.
          """.format(GUESS_DIGITS), end='')
    
    while True:
        try:
            user_guess = ""
            i = 1
            computer_num = get_computer_num()
            print()
            while user_guess != computer_num and  i <=  NUM_GUESSES:
                print("Guess #{}".format(i))
                user_guess = get_user_guess()
                print(getClues(user_guess, computer_num))

                if i == NUM_GUESSES and user_guess != computer_num:
                    print("You are out of guesses 💔!")
                    print("The number was {}".format(computer_num))

                i+=1 

            print("Do you want to continue ? (y/n)")
            if not input("> ").lower().startswith("y"):
                raise KeyboardInterrupt

        except (EOFError, KeyboardInterrupt):
            print("Thanks for playing!")
            break
    


def get_computer_num():
    """Returns a secret number generated by computer."""
    nums = [str(x) for x in range(10)]
    computer_num = ""
    shuffle(nums)

    for i in range(GUESS_DIGITS):
        computer_num += nums[i]
    return computer_num

def getClues(user_num, secret_num):
    "Generates and Returns strings based on users guesses to suggest hints."
    if user_num == secret_num:
        return "You got it!" 
    
    clues=[]
    for i in range(len(user_num)):
        if user_num[i] in secret_num:
            if user_num[i] == secret_num[i]:
                clues.append("Fermi")
            else:
                clues.append("Pico")
    if len(clues) == 0:
        clues.append("Bagel")
    clues.sort()
    return clues


def get_user_guess():
    """Prompts and processes user's guess/input."""
    user_guess = input("> ")

    while not(len(user_guess) == GUESS_DIGITS and user_guess.isdecimal() ):
        print(f"Digits must be a decimal number and {GUESS_DIGITS} in length.", file=sys.stderr)
        user_guess = input("> ")
    return user_guess
            
if __name__ =="__main__":
    main()

    