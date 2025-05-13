def addtoarray(a):
    length = len(a)

    if length == 1:
        return a[0]
    return a[0] + addtoarray(a[1:])

a = [1, 2, 3, 4, 5]

print("\n Sum of array is ", addtoarray(a))