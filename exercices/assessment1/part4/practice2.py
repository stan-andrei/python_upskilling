import random

'''
Write a Python program to guess a number between 1 to 9. 
User is prompted to enter a guess. 
If the user guesses wrong then the prompt appears again until the guess is correct, 
on successful guess, user will get a "Well guessed!" message, and the program will exit.
'''

if __name__ == "__main__":

    print("The game of guessing the number!")
    print("Rules: Guess a number between 1 and 9")
    print("Good luck!")
    random_num, guess_num = random.randint(1, 9), 0
    while random_num != guess_num:
        guess_num = int(input('Enter a number: '))
    print('Well guessed!')

input("Press any key to exit")
