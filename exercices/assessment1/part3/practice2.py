

if __name__ == "__main__":
    """Create a program that gets a message from the user and then prints it out backwards."""
    message = input("Put your message here and we will print it out backwards: ")
    print("".join(reversed(message)))

input("Press any key to exit")
