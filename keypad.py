keypad = ["","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

def printcombo(combination,curr,output,n):
    if (curr == n):
        print(*output,sep=",")
        return
    for i in range(len(keypad[combination[curr]])):
        output.append(keypad[combination[curr]][i])
        printcombo(combination,curr+1,output,n)
        output.pop()
        if (combination[curr] == 0 or combination[curr] == 1):
            return
        
combination = [2,3,3]
printcombo(combination,0,[],len(combination))