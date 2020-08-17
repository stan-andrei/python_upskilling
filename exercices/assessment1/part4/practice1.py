
'''Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
 between 1500 and 2700 (both included).'''

if __name__ == "__main__":

    num_list = []
    for i in range(1500, 2701):
        if i % 7 == 0 and i % 5 == 0:
            num_list.append(i)
    print(num_list)

input("Press any key to exit")

