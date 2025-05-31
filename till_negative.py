def take_input():
    num = int(input("Enter a number (negative to stop): "))
    if num < 0:
        print("Negative number entered. Stopping.")
        return
    else:
        take_input()
        
take_input()
