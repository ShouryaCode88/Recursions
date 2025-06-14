def subarray(arr,n,sum_):
    for i in range(n):
        curr_sum = arr[i]

        j = i+1
        while j <= n:
            if curr_sum == sum_:
                print("Sum found between %d and %d" %(i,j+1))
                return 1
            if curr_sum >= sum_ or j == n:
               break
            curr_sum = curr_sum + arr[j]
            j += 1
    print("Not found")
    return 0    

arr = [1,4,5,-3,4,8,-9,-1,3,3,5]
n = len(arr)

sum_ = 7
subarray(arr,n,sum_)
