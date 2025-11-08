def pritnA(i, j):
    return ((j == 0 and i != 0)or
            (j == 6 and i != 0) or
            (i == 0 and 0<j<6)or
            (i == 3 and 0<j<6))

def printB(i, j):
    return((j == 0) or
           (i == 0 and 0<j<6) or
           (i == 3 and 0<j<6) or
           (i == 6 and 0<j<6) or
           (j == 6 and i not in [0,3,6]))
def printD(i, j):
    return((j == 0) or
           (i == 0 and 0<j<6) or
           (i == 6 and 0<j<6) or
           (j ==6) and i not in [0,6])

def pritnE(i, j):
    return((j == 0) or
           (i == 0 and j<=6)or
           (i == 3 and j<5)or
           (i == 6 and j<=6))

def printL(i, j):
    return((j == 0)or
           (i == 6 and j<=6))

def printI(i, j):
    return((i == 0) or (i == 6) or (j == 3))

for i in range(7):
    for j in range(7):
        print("*" if pritnA(i, j) else " ", end="")
    print("  ", end="")
    
    for j in range(7):
        print("*" if printB(i, j) else " ", end="")
    print("  ", end="")

    for j in range(7):
        print("*" if printD(i, j) else " ", end="")
    print("  ", end="")

    for j in range(7):
        print("*" if pritnE(i, j) else " ", end="")
    print("  ", end="")

    for j in range(7):
        print("*" if pritnA(i, j) else " ", end="")
    print("  ", end="")

    for j in range(7):
        print("*" if printL(i, j) else " ", end="")
    print("  ", end="")
    
    for j in range(7):
        print("*" if printI(i, j) else " ", end="")
    print("  ", end="")

    print()