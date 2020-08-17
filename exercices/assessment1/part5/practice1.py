import random

'''
Create a program that prints a list of random words.
The program should print all the words and not repeat any.
 '''

if __name__ == "__main__":

    words = ["Hello", "Sun", "Iris", "Rain", "Flower"]
    new = []

    while len(new) != len(words):
        choice = random.choice(words)
        if choice not in new:
            print(choice)
            new.append(choice)

input("Press any key to exit")
