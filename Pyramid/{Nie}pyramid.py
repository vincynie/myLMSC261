stacks = int(input('Enter the number of stacks between 1 to 8: '))
if stacks >= 9:
    print("stacks out of range, please exit the program")
else:
    for i in range(0, stacks):
        for j in range(stacks, -1, -1):
            if j>i:
                print("", end = '')
            else:
                print('#', end='')
        print("")
            
