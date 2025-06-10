def getmaxones(a,a_size):
    counter = 0
    maxOnes = 0

    for i in range(0,a_size):
        if a[i] == 0:
            counter = 0
        else:
            counter += 1
            max_one = max(maxOnes,counter)

    return max_one

a = [1,1,0,0,1,0,1,1,1,1,1] 
a_size = len(a)

print("Max 1's are :- ", getmaxones(a,a_size))