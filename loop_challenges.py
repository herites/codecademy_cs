# Write your function here
def divisible_by_ten(nums):
    return len([x for x in nums if x % 10 == 0])


# Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
# Write your function here
def add_greetings(names):
    return ["Hello, " + x for x in names]


# Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))
# Write your function here
def delete_starting_evens(lst):
    try:
        while lst[0] % 2 == 0:
            lst.pop(0)
    except IndexError:
        print("Out of nums!")
    return lst


# Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
# Write your function here
def odd_indices(lst):
    return [value for index, value in enumerate(lst) if index % 2 != 0]


# Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
# Write your function here
def exponents(bases, powers):
    raised = []
    for i in bases:
        for j in powers:
            raised.append(i ** j)
    return raised


# Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
