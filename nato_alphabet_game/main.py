import pandas

alphabet_file = pandas.read_csv("./nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in alphabet_file.iterrows()}
user_input = input("Enter your name -> ").upper()
result = [phonetic_dict[letter] for letter in user_input]

print(result)
