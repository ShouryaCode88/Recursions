def reversestring(s):
    if len(s) == 1:
        return s[0]
    
    first = s[0]

    return reversestring(s[1:]) + first

s = input("Enter a string to reverse:- ")
print(reversestring(s))