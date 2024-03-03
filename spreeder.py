#Built-in Imports
import argparse
from os import path
from sys import argv, exit


# Add command-line args to ease testing? Mainly for file testing
def main():

    #Initialize the command-line arguments
    args = init_command_line_args()

    words = []

    if len(argv) == 1:
        exit("Incorrect number of arguments!")


    if args.file:
        file_name = input("Filename (.txt files only): ")
        #Catch error
        #delay_length = float(input("Decimal delay (s): "))
        #Catch error
        #num_words_per_frame = int(input("Num of words per frame: "))

        file_size = path.getsize(file_name)

        #Try -> FileNotFoundError?
        with open(file_name) as file:
            word = ""
            for _ in range(file_size):
                #char
                c = file.read(1)

                #Detects breaks between words/punctuation
                #Goal -> Append each character until whitespace detected -> Add full word to list
                if not c.isspace():
                    print(f"True, {c}")
                    word += c
                else:
                    words.append(word)
                    word=""

        for i, v in enumerate(words):
            print(i, v)
    elif args.internet:
        print("Not implemented yet.")
    elif args.user:
        print("Not implemented yet.")


#Initializes the command-line args for this specific program
def init_command_line_args():
    parser = argparse.ArgumentParser(description="Usage: spreeder.py [FILE]\nProgram designed to improve reading speed.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f", "--file", help="read from a .txt file", action='store_true')
    group.add_argument("-i", "--internet", help="display text from an internet link", action='store_true')
    group.add_argument("-u", "--user", help="display user-input", action='store_true')

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()
