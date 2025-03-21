# Claire Francis, March 20th, 2025, Week8_program2.py

# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together,
# but the first character of each word is uppercase.
# Convert the sentence to a string in which the words are separated by spaces,
# and the first word starts with an uppercase.
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):
    new_sentence = ""
    #    Add your logic here


    # coppy first letter of user_input into the result variable
    new_sentence += user_input[0]

    for i in range(1, len(user_input)):
        char = user_input[i]

        # if the next character is in uppercase insert a space
        # for the new word and convert the letter to lower case.
        if char.isupper():
            new_sentence += ' '
            char = char.lower()
            new_sentence += char
        else:
            new_sentence += char

    return new_sentence.strip()

if __name__ == '__main__':
    user_input = input('Enter a string: ')
    print(word_separator(user_input))

# Example usage

sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)
