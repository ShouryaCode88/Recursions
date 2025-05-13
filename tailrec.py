def tailrec(n,num):
    if n > num:
        return
    print(n)
    tailrec(n+1,num)

n = int(input("Enter a n to print from 1 to n:- "))
tailrec(1,n)