def decimal_to_binary(n):
    if n==0:
        return 0
    else:
        return n%2 + 10 * decimal_to_binary(n//2)
    
    

n = int(input("Enter n:- "))
print(decimal_to_binary(n))