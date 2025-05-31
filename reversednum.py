def reversednumber(num):
    if num > 0:
        last = num % 10
        if (num // 10 > 0):
            current_num = reversednumber(num // 10)
            return last * pow(10,len(str(current_num))) + current_num
        return num
    
num = int(input("Enter a number to reverse:- "))
print(reversednumber(num))