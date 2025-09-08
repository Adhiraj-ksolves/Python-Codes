# tuple to list
def tuple_to_list(t):
    return list(t)

# list to set
def list_to_set(lst):
    return set(lst)

# set to tuple
def set_to_tuple(s):
    return tuple(s)


my_tuple = (1, 2, 3, 4)
my_list = [1, 2, 2, 3, 4]
my_set = {5, 6, 7}

print("Tuple to List:", tuple_to_list(my_tuple))
print("List to Set:", list_to_set(my_list))
print("Set to Tuple:", set_to_tuple(my_set))
