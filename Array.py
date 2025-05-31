def mean_array(arr,arr_length):
    total_sum = 0
    for i in range(0,arr_length):
        total_sum += arr[i]
    return total_sum/arr_length

def median_array(arr,arr_length):
    arr.sort()
    
    if arr_length % 2 != 0:
        return float((arr[int[arr_length/2]])) 
    return float((arr[int(arr_length-1/2)] +  arr[int(arr_length/2.0)])/2.0)

arr = [2,5,6,1]
arr_length = len(arr)

print("Mean :-",mean_array(arr,arr_length))
print("Median :-",median_array(arr,arr_length))