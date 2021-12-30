# Write your word_length_dictionary function here:
def word_length_dictionary(words):
    return dict(zip(words, [len(x) for x in words]))


# Uncomment these function calls to test your  function:I
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}
# Write your frequency_dictionary function here:
def frequency_dictionary(words):
    return dict(zip(words, [words.count(x) for x in words]))


# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0, 0, 0, 0, 0]))
# should print {0:5}
# Write your unique_values function here:
def unique_values(my_dict):
    return len(set(my_dict.values()))


# Uncomment these function calls to test your  function:
print(unique_values({0: 3, 1: 1, 4: 1, 5: 3}))
# should print 2
print(unique_values({0: 3, 1: 3, 4: 3, 5: 3}))
# should print 1
# Write your count_first_letter function here:
def count_first_letter(names):
    return_dict = {x[0]: 0 for x in names.keys()}
    for key, value in names.items():
        return_dict[key[0]] += len(value)
    return return_dict


# Uncomment these function calls to test your  function:
print(
    count_first_letter(
        {
            "Stark": ["Ned", "Robb", "Sansa"],
            "Snow": ["Jon"],
            "Lannister": ["Jaime", "Cersei", "Tywin"],
        }
    )
)
# should print {"S": 4, "L": 3}
print(
    count_first_letter(
        {
            "Stark": ["Ned", "Robb", "Sansa"],
            "Snow": ["Jon"],
            "Sannister": ["Jaime", "Cersei", "Tywin"],
        }
    )
)
# should print {"S": 7}
