
"""Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list. For practice,
write this code inside a function.
"""

if __name__ == "__main__":
    a = [5, 10, 15, 20, 25]
    def new_list(a):
        return [a[0], a[- 1]]
    print(new_list(a))

input("Press the enter key to exit.")
