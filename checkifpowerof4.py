n = int(input("Enter a number to check if it is a power of 4:- "))

def powerof4(n):
    if (n<=0):
        return False
    if (n == 1):
        return True
    if (n%4 == 0 ):
        return powerof4(n//4)
    return False

if powerof4(n):
    print(f"{n} is a power of 4")
else:
    print(f"{n} is not a power of 4")
