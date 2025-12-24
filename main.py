x=int(input())
for i in range(1,x+1):
    if (i%3==0)and(i%5==0):
        print("fizz buzz")
    elif i%5==0:
        print("buzz")
    elif(i%3==0):
        print("fizz")
    else:
        print(i)   

#patterns
1.
x=int(input())
for i in range(x):
    for j in range(x):
        print("*",end=" ")
    print()
  
2.
x=int(input())
for i in range(x):
    for j in range(i+1):
         print("*",end=" ")
    print()

3.
x=int(input())
for i in range(x):
    for j in range(i+1):
         print("*",end=" ")
    print()


    
