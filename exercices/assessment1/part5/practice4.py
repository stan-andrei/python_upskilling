"""
Improve the Who’s Your Daddy program by adding a choice that lets the user enter a name and get back a grandfather.
 Your program should still only use one dictionary of son-father pairs.
 Make sure to include several generations in your dictionary so that a match can be found.
"""

if __name__ == "__main__":
    names = {"Tony Stark": "Howard Stark",
             "Howard Stark": "Ben Stark",
             "Thor": "Odin",
             "Odin": "Bor",
             "Peter Parker": "Richard Parker",
             "Richard Parker": "Tom Parker",
             "Bruce Wayne": "Thomas Wayne",
             "Thomas Wayne": "Nick Wayne",}
    choice = None
    while choice != "Q":
        print(
            """
        The Game of Who's his Father or Grandfather?
    
        Q - Quit
        P - Play
        A - Add 
        D - Delete 
        R - Replace 
        G - Grandfather

        """
        )
        choice = input("Enter a letter: ")
        print()
        if choice == "Q":
            print("See you soon")
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
        elif choice == "G":
            pick = input("Enter a name:")
            if pick in names:
                father = names[pick]
                if father in names[pick]:
                    grandfather = names[father]
                print(pick, "is the grandson of", grandfather)
            else:
                print("Your name is not in the list!")
        else:
            print( choice, "isn't a choice. Enter a valid choice.")

input("Press the enter key to exit.")
