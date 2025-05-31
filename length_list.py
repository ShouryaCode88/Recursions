def recursive_length(lst):
    # Base case: if the list is empty, length is 0
    if lst == []:
        return 0
    else:
        return 1 + recursive_length(lst[1:])

my_list = [1, 2, 234, 234, 745, 3, 6, 653]
length = recursive_length(my_list)
print("Length of the list:", length)
