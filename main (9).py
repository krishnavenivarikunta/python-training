
x=int(input())
for i in range(x):
    for j in range(x-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
        x=int(input())
for i in range(x):
    for j in range(x-2-1,-1):
        print(" ",end=" ")
    for j in range(x+1):
        print("*",end=" ")
    print()