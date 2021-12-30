# Write your sum_values function here:
def sum_values(my_dict):
    return sum(my_dict.values())


# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
# should print 10
print(sum_values({10: 1, 100: 2, 1000: 3}))
# should print 6
# Write your sum_even_keys function here:
def sum_even_keys(my_dict):
    return sum([value for key, value in my_dict.items() if key % 2 == 0])


# Uncomment these function calls to test your  function:
print(sum_even_keys({1: 5, 2: 2, 3: 3}))
# should print 2
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))
# should print 6
def add_ten(my_dict):
    return {key: value + 10 for key, value in my_dict.items()}


# Uncomment these function calls to test your  function:
print(add_ten({1: 5, 2: 2, 3: 3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10: 1, 100: 2, 1000: 3}))
# should print {10:11, 100:12, 1000:13}
# Write your values_that_are_keys function here:
def values_that_are_keys(my_dict):
    return [x for x in my_dict.values() if x in my_dict.keys()]


# Uncomment these function calls to test your  function:
print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
# should print [1, 4]
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
# should print ["a"]
# Write your max_key function here:
def max_key(my_dict):
    return [x[0] for x in my_dict.items() if x[1] == max(my_dict.values())][0]


# Uncomment these function calls to test your  function:
print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
# should print 1
print(max_key({"a": 100, "b": 10, "c": 1000}))
# should print "c"
