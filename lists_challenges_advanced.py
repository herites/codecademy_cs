# Write your function here
def every_three_nums(start):
    lst = []
    if start > 100:
        return lst
    else:
        while start <= 100:
            lst.append(start)
            start += 3
    return lst


# Uncomment the line below when your function is done
print(every_three_nums(91))
# Write your function here
def remove_middle(list, start, end):
    return [x for x in list if x not in list[start : end + 1]]


# Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
# Write your function here
def more_frequent_item(lst, item1, item2):
    return item1 if lst.count(item1) >= lst.count(item2) else item2


# Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
# Write your function here
def double_index(lst, index):
    new_lst = []
    if index >= len(lst):
        return lst
    else:
        for count, value in enumerate(lst):
            if count != index:
                new_lst.append(value)
            else:
                new_lst.append(value * 2)
    return new_lst


# Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
# Write your function here
def middle_element(lst):
    return (
        lst[int(len(lst) / 2)]
        if len(lst) % 2 != 0
        else sum(lst[int(len(lst) / 2) - 1 : int(len(lst) / 2) + 1]) / 2
    )


# Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
