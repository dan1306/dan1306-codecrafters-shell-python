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

        for i in range(50):
            print(user_Input[0])

        if(user_Input == "exit 0"):
            sys.exit(0)
        elif(user_Input[0] == "echo"):
            print_this_out = ""
            for i in range(1, len(user_Input)):
                print_this_out+= i
            print(print_this_out)
        else:
            print(f"{user_Input}: command not found")


if __name__ == "__main__":
    main()
