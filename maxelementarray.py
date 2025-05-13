def maxelementarray(a):
    length = len(a)

    if length == 1:
        return a[0]
    return max(a[0], maxelementarray(a[1:]))

a = [1,783,256,99,4]
print("\n Maximum element of array is ", maxelementarray(a))