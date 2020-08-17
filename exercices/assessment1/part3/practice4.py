'''Write a Python program to construct the following pattern:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

if __name__ == "__main__":

    rows = 5
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("*", end=' ')
        print("\r")

    for i in range(rows, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print("\r")

input("Press any key to exit")
