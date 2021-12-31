letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
    counter = 0
    word_lst = []
    for i in word:
        if i not in word_lst:
            word_lst.append(i)
    for i in word_lst:
        if i in letters:
            counter += 1
    return counter


# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
# Write your count_char_x function here:
def count_char_x(word, x):
    return word.count(x)


# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
    return word.count(x)


# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1
# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
    return (
        word
        if (start not in word or end not in word)
        else word[word.find(start) + 1 : word.find(end)]
    )


# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
# Write your x_length_words function here:
def x_length_words(sentence, x):
    return True if False not in [len(word) >= x for word in sentence.split()] else False


# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
