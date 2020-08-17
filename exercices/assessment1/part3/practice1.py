

if __name__ == "__main__":
    """Write a program that counts for the user. Let the user enter the starting number, the ending number, 
    and the amount by which to count."""

    start = int(input("Starting number:  "))
    end = int(input("Ending number: "))
    count = int(input("Amount by which to count: "))

    for i in range(start, end+1, count):
        print(i)

input("Press any key to exit")
