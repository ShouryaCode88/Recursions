def leaders(a,a_size):
    currentmax = a[a_size-1]
    print(currentmax)

    for i in range(a_size-2,-1,-1):
        if currentmax < a[i]:
            currentmax = a[i]
            print(currentmax)

a = [1,4,9,11,45,3]

leaders(a,len(a))