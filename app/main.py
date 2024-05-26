import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("$ ")

    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")
    # sys.stdout.flush()
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    user_Input = input()
    print({user_Input} + ": command not found")


if __name__ == "__main__":
    main()
