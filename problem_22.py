'''
Problem 22

@author: Kevin Ji
'''


def get_value_of_letter(letter):
    return ord(letter.upper()) - 64


def get_value_of_word(word):
    value = 0

    for char in word:
        value += get_value_of_letter(char)

    return value

# Parse the file, and place the names into a list
file = open("problem_22_names.txt", "r")
names_text = file.read()
names = sorted(names_text.replace("\"", "").split(","))

# Values and scores of names
values = [get_value_of_word(name) for name in names]
scores = [value * (rank + 1) for value, (rank, name) in zip(values, enumerate(names))]

print(sum(scores))
