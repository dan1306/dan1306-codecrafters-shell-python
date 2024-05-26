import sys

def split_with_spaces(input_string):
    result = []
    word = ''
    for char in input_string:
        if char == ' ':
            if word:
                result.append(word)
                word = ''
            result.append(' ')
        else:
            word += char
    if word:
        result.append(word)
    return result

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

        user_input_for_echo = split_with_spaces(user_Input)
        
        if(user_input_for_echo[0] == "type"):
            if(user_input_for_echo[2] == "echo"):
                print("echo is a shell builtin")
            elif(user_input_for_echo[2] == "exit"):
                print("exit is a shell builtin")
            elif(user_input_for_echo[2] == "type"):
                print("type is a shell builtin")
            elif(user_input_for_echo[2] == "nonexistent"):
                print("type is a shell builtin")
        else:
            if(user_Input == "exit 0"):
                sys.exit(0)
            elif(user_input_for_echo[0] == "echo"):
                print_this_out = "".join(user_input_for_echo[1:])
                print(print_this_out)
            else:
                print(f"{user_Input}: command not found")


if __name__ == "__main__":
    main()
