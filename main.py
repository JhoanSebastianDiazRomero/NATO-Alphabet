import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)


def generate_phonetic():
    try:
        user_input = input("Input a word to get NATO version: ").upper()
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        nato_input = [nato_dict[letter] for letter in user_input]
        print(nato_input)

generate_phonetic()