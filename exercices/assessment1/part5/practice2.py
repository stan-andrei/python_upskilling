
'''
Create a program that computes the sum of all float and integer numbers from a list.
The given list contains other data types as well: strings, tuples, list of lists, etc.
(e.g: at least one list element from each data type + combinations
(e.g: one element with list of numbers))
'''

if __name__ == "__main__":

    lists = ['foo', 1, 'bar', 3.2, 4, (3, "eu"), [3, 4]]
    sum = 0
    for i in lists:
        if isinstance(i, int) or isinstance(i, float):
            sum += float(i)
        else:
            for j in i:
                if isinstance(j, int) or isinstance(j, float):
                    sum += float(j)
    print(sum)

input("Press any key to exit")
