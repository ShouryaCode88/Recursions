def max_diff(a):
    min_val = a[0]
    max_diff = 0
    for i in range(1, len(a)):
        if a[i] - min_val > max_diff:
            max_diff = a[i] - min_val
        if a[i] < min_val:
            min_val = a[i]
    return max_diff


a = [4,5,234,2,6,82,234,5234]

print("Max difference:- ",max_diff(a))