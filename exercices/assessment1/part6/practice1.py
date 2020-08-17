
"""
Write a function which computes the sum of n numbers. n is sent as a parameter via the command line.
"""

print("The program that sums the digits of a given number! ")
n = input("Enter a 2 or more digit number: ")

def digit_sum(n):
    num_str = str(n)
    sum = 0
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
    return sum

if __name__ == "__main__":
    print(digit_sum(n))

input("Press the enter key to exit.")
