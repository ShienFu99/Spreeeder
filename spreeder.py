# Built-in Imports
import argparse
from getpass import getpass
from os import path, system
from sys import argv, exit
from time import sleep

# Add a 3 second delay before reading out text + start on first word
# Account for errors in the future (FileNotFound, ValueError, Etc)
def main():

    args = init_command_line_args()

    # List containing words from given source (file, user-input)
    words = []
    word = ""

    # Prompts user to relaunch program if no flags are used
    if len(argv) == 1:
        exit("Relaunch program with a flag. Use -h if you need help.")

    while True:
        try:
            delay_length = float(input("Decimal delay (s): "))
            break
        except ValueError:
            clear_console()
            print("Invalid value!")
            pass

    # GET user values for num_words_per_print -> Ensure num of words is compatible with length of file
    #num_words_per_frame = int(input("Num of words per frame: "))

    # Fully functional
    if args.file:

        # Prompts user for name of file
        file_name = input("Filename (.txt files only): ").lower().strip()

        # Get the size of the file in bytes -> 1 char == 1 byte
        file_size = path.getsize(file_name)

        # Functioning - If file is empty, exit program
        if not file_size:
            exit("File is empty!")

        # Functioning - If file ext is not .txt, exit program
        if not file_name.endswith(".txt"):
            exit("File is not a .txt file!")

        # WIP: Catch FileNotFoundError
        with open(file_name) as file:
            for _ in range(file_size):
                #char
                ch = file.read(1)

                #Detects breaks between words/punctuation
                #Goal -> Append each character until whitespace detected -> Add full word to list
                if not ch.isspace():
                    # Testing purposes only
                    #print(f"True, {ch}")
                    word += ch
                else:
                    words.append(word)
                    word=""

    # Allow the user to input text to be read back to them
    elif args.user:
        user_text = input("Text: ")

        for i, ch in enumerate(user_text):
            #Detects breaks between words/punctuation

            # input() does not capture \n char -> When final character is reached, append word to list
            if i == len(user_text) - 1:
                if not ch.isspace():
                    word += ch
                words.append(word)
                word=""
                break

            if not ch.isspace():
                word += ch
            else:
                words.append(word)
                word=""

    for i, v in enumerate(words):
        sleep(delay_length)
        clear_console()
        print(v)

    proceed(1)


# Clears the console
def clear_console():
    system("clear")


# Initializes command-line args
def init_command_line_args():
    parser = argparse.ArgumentParser(description="Usage: spreeder.py [FILE]\nProgram designed to improve reading speed.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f", "--file", help="read from a .txt file", action='store_true')
    group.add_argument("-u", "--user", help="display user-input", action='store_true')

    args = parser.parse_args()

    return args


#Press Enter to continue -> If int_exit is set to 1, exit the program, else program continues
def proceed(int_exit):
    #Hides + discards user input -> Program pauses until the user presses Enter
    getpass("\nPress enter to continue...")
    clear_console()
    if int_exit:
        exit()


if __name__ == "__main__":
    main()
