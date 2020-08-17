import random

if __name__ == "__main__":

    '''Create a game where the computer picks a random word and the player has to guess that word. 
    The computer tells the player how many letters are in the word. 
    Then the player gets five chances to ask if a letter is in the word. The computer can only respond with “yes” or “no”.
     Then, the player must guess the word.
    '''

dic = ("apple","sun","moon","iris","love","wall")

word = random.choice(dic)
word_len = len(word)
letter = 0
attempt = 0
temp = "-" * word_len

print("The word contain", word_len,"letters.")
print("Tap any letter")
print("You got 5 attempts")


for i in range(0, 5):
    attempt += 1
    letter = input("Attempt " + str(attempt) + ":")
    if letter in word:
        for i in range(0, word_len):
            if letter == word[i]:
                temp = temp[:i] + letter + temp[i+1:]
        print("yes\n" + temp)
    if letter not in word:
        print("no")
    if "-" not in temp:
        print("You guess the word!")
        break
    elif attempt == 5:
        letter = input("Enter the word:")
        if letter == word:
            print("You guess the word")
        else:
            print("You guess wrong")

input("Press any key to exit")

