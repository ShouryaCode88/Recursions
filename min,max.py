def min_element(a,size):
    temp = a[0]

    for i in range(1,size):
        temp = min(temp,a[i])
    
    return temp

def max_element(a,size):
    temp = a[0]

    for i in range(1,size):
        temp = max(temp,a[i])
    
    return temp


a = [4,5,13,89,14,6,4,1,2,0]
size = len(a)

print("Min element:-",min_element(a,size))
print("Max element:-",max_element(a,size))
