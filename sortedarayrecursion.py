def checksorted(a):
    length = len(a)

    if length == 1 or length == 0:
        return True
    return a[0] <= a[1] and checksorted(a[1:])

a = [1, 2, 3, 4, 8,2]

if checksorted(a):
    print("\n Array is sorted")
else:
    print("\n Array is not sorted")