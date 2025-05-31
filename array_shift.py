def rotation(a,n,a_size):
    for i in range(n):
        rotate(a,a_size)

def rotate(a,a_size):
    temp = a[0]
    for i in range(a_size-1):
        a[i] = a[i+1]
    a[i + 1] = temp
    print("\nNew array")
    for i in range(a_size):
        print(a[i],end = ' ')

a = [1,2,5,124,6,8]
a_size = len(a)

rotation(a,2,a_size)

