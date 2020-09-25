def firstpart(n):
    for i in range(0,n):
        for j in range(0, i+1):
            print("*", end="")
        print("\r")
        
firstpart(5)

def secondpart(i):
    for i in range(0,i,-1):
        for j in range(0,i+1):
            print("*", end="")
        print("\r")
secondpart(4)