# Write your function here
def larger_sum(lst1, lst2):
    return lst1 if sum(lst1) >= sum(lst2) else lst2


# Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
# Write your function here
def over_nine_thousand(lst):
    power_level = 0
    for i in lst:
        if power_level < 9000:
            power_level += i
    return power_level


# Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
# Write your function here
def max_num(lst):
    max_num = lst[0]
    for i in lst:
        if i > max_num:
            max_num = i
    return max_num


# Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
# Write your function here
def same_values(lst1, lst2):
    return [index for index, value in enumerate(lst1) if lst1[index] == lst2[index]]


# Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
# Write your function here
def reversed_list(lst1, lst2):
    return lst1 == lst2[::-1]


# Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
