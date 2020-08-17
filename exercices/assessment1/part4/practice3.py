
'''Write a Python program to print messages on the screen as long as a condition is met'''

if __name__ == "__main__":
    print("Even or Odd number checker!")
    print("Enter any number you can think of, and the program will tell you if is an even or odd number")

    num = int(input("Your number: "))
    if (num % 2) == 0:
        print("{0} is Even number".format(num))
    else:
        print("{0} is Odd number".format(num))

input("Press any key to exit")