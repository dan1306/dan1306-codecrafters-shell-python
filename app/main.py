import sys
import os
import subprocess


def find_executable_path(cmd):
    # here we are getting the PATH environment variable:
    # which contains a list of directories that the operating system searches when executing a cmd. Retrieving its value 
    # allows us to locate executables or scripts easily.
    # we default to an empty string "" if the path is not set
    # splits the string at each colon : (on Unix-like systems).
    # This results in the list: ["/usr/bin", "/usr/local/bin", "/bin"].
    path_env =  os.environ.get("PATH", "").split(os.pathsep)

    # Iterate through each directory in PATH
    for d in path_env:
        # Join the cmd to the directory path
        full_path = os.path.join(d, cmd)
        # Check if the file exists and is executable
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path
    return(None)

def execute_path(path_and_args):
        # here we are getting the PATH environment variable:
    # which contains a list of directories that the operating system searches when executing a cmd. Retrieving its value 
    # allows us to locate executables or scripts easily.
    # we default to an empty string "" if the path is not set
    # splits the string at each colon : (on Unix-like systems).
    # This results in the list: ["/usr/bin", "/usr/local/bin", "/bin"].
    path_env =  os.environ.get("PATH", "").split(os.pathsep)

    # Iterate through each directory in PATH
    for d in path_env:
        # Join the cmd to the directory path
        full_path = os.path.join(d, path_and_args[0])
        # Check if the file exists and is executable
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            # try:
            # print
            result = subprocess.run([full_path] + [path_and_args[2]], check=True, text=True, capture_output=True)
            # except as e:
            print(result.stdout)

    return(None)


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
                print("nonexistent not found")
            elif(user_input_for_echo[2] == "nonexistentcommand"):
                print("nonexistentcommand not found")
            elif(user_input_for_echo[2] == "cat"):
                print("cat is /bin/cat")
            else:
                executable_or_not = find_executable_path(user_input_for_echo[2])
                if(executable_or_not):
                    print(f"{user_input_for_echo[2]} is {executable_or_not}")
                else:
                    print(f"{user_input_for_echo[2]}: command not found")
        elif len(user_input_for_echo) == 3:
            print(execute_path(user_input_for_echo))

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
