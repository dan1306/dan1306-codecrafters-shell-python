import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("$ ")

    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")
    # sys.stdout.flush()
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user_Input = input()

        if(user_Input == "exit 0"):
            sys.exit(0)
        else:
            print(f"{user_Input}: command not found")


if __name__ == "__main__":
    main()
