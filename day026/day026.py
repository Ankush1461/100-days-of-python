# NATO Alphabet Program

import pandas

# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}  # Dictionary comprehension
print(phonetic_dict)


def generate_phonetic():
    # Create a list of the phonetic code words from a word that the user inputs.
    word = input("Enter a word: ").upper()
    try:          # Included try-catch block on day 30
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
