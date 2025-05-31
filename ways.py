def ways(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    
    onestep = 0
    twostep = 0

    if stairs >= 2:
        twostep = ways(stairs - 2)
    
    onestep = ways(stairs-1)

    return onestep + twostep

stairs = int(input("Enter the number of stairs: "))
print(f"Number of ways to climb {stairs} stairs: {ways(stairs)}")