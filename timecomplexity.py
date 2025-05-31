#Func 1

def fac(n):
    if n == 0 or n == 1:
        return 
    return n * fac(n - 1)
 
print("O(1)")
# Time complexity == 1

#Func 2 

def print1to10(n):

    if n>10:
        return
    print(n)
    print1to10(n+1)

print(print1to10(2))

print("O(n)")
# Time complexity == n