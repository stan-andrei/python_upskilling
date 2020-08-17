
''''
Write a Who’s Your Daddy? program that lets the user enter the name of a male and produces the name of his father.
(You can use celebrities, fictional characters, or even historical figures for fun.)
Allow the user to add, replace, and delete son- father pairs.
'''

if __name__ == "__main__":
    names = {"Tony Stark": "Howard Stark.",
             "Thor": "Odin",
             "Peter Parker": "Richard Parker",
             "Bruce Wayne": "Thomas Wayne", }
    choice = None
    while choice != "Q":
        print(
            """
        The Game of Who's his Father?
        L - List
        Q - Quit
        P - Play
        A - Add 
        D - Delete 
        R - Replace 

        """
        )
        choice = input("Choice: ")
        print()
        if choice == "Q":
            print("See you soon")
        elif choice == "L":
            print("List of people you can find who their father is:")
            for key in names:
                print(key)
        elif choice == "P":
            pick = input("Enter a name: ")
            if pick in names:
                father = names[pick]
                print(pick, "is the son of", father)
            else:
                print(pick, "is not in the list, enter another name ")
        elif choice == "A":
            pick = input("Add a son: ")
            if pick not in names:
                father = input("Add a father: ")
                names[pick] = father
                print("You add ", pick, "to the list.")
            else:
                print("Already in the list")
        elif choice == "D":
            pick = input("Enter the name to deleted: ")
            if pick in names:
                del names[pick]
                print("You deleted", pick, "from the list.")
            else:
                print("Your name is not in the list!")
        elif choice == "R":
            pick = input("Enter a name to replace: ")
            if pick in names:
                father = input("Enter new father?: ")
                names[pick] = father
                print(pick, "has a new father.")
            else:
                print("Your name is not in the list!")
        else:
            print("Sorry,", choice, "isn't a choice. Enter a valid choice.")

input("Press the enter key to exit.")
