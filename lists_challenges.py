# Write your function here
def append_size(lst):
    lst.append(len(lst))
    return lst


# Uncomment the line below when your function is done
print(append_size([23, 42, 108]))
# Write your function here
def append_sum(lst):
    counter = 0
    while counter < 3:
        counter += 1
        lst.append(sum(lst[-2:]))
    return lst


# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
# Write your function here
def larger_list(lst1, lst2):
    return lst2[-1] if len(lst2) > len(lst1) else lst1[-1]


# Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
# Write your function here
def more_than_n(lst, item, n):
    return lst.count(item) > n


# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
# Write your function here
def combine_sort(lst1, lst2):
    return sorted(lst1 + lst2)


# Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
