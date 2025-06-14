def equilibrium(arr):
    leftsidesum = 0
    rightsidesum = 0
    n = len(arr)

    for i in range(n):
        leftsidesum = 0
        rightsidesum = 0

        for j in range(i):
            leftsidesum += arr[j]
        
        for j in range(i+1,n):
            rightsidesum += arr[j]

        if leftsidesum == rightsidesum:
            return i
    
    return -1

arr = [11,10,2,9,11,1]
print("Element: ", arr[equilibrium(arr)])