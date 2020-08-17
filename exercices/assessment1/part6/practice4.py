
"""
Write a Python program to execute a string containing Python code.
"""

if __name__ == "__main__":
    code = '''
for i in range(20):
    if (i%2 == 0):
        print(i)
        '''
    exec(code)

input("Press the enter key to exit.")
