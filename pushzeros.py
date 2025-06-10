def pushzero(a,a_size):
    zero = 0
    nonzero = 0

    while(nonzero!=a_size):
        if a[nonzero]!=0:
           a[nonzero],a[zero] = a[zero],a[nonzero]
           zero += 1
        
        nonzero += 1


a = [1,0,4,1,0,0,0,1,0,4,5,0,0,1,9]
a_size = len(a)

print(a)

pushzero(a,a_size)

print("Zeroes after pushing it to left:")

print(a)
