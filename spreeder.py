#Imports
import os


def main():
    words = []

    file_name = input("Filename (.txt files only): ")
    #Catch error
    delay_length = float(input("Decimal delay (s): "))
    #Catch error
    num_words_per_frame = int(input("Num of words per frame: "))

    file_size = os.path.getsize(file_name)

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


if __name__ == "__main__":
    main()
