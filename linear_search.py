def search(arr,n,x):
    for i in range(0,n):
        if (arr[i] == x):
            return i 
    return -1

arr = [10,9,1,3,6,4]
x = int(input("Enter your number:- "))
n = len(arr)

result = search(arr,n,x)

if result == -1:
    print("Elemnt not found in array!")
else:
    print("Array found at index:- ",result)