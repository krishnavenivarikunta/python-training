1.FIZZ BUZZ
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
1.SQUARE
x=int(input())
for i in range(x):
    for j in range(x):
        print("*",end=" ")
    print()
  
2.TRIANGLE
x=int(input())
for i in range(x):
    for j in range(i+1):
         print("*",end=" ")
    print()

3.NUMBERS
x=int(input())
for i in range(x):
    for j in range(i+1):
         print("*",end=" ")
    print()

4.DIMOND PATTERN
x=int(input())
for i in range(x):
    for j in range(x-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
  for i in range(x-2,-1,-1):
    for j in range(x-i-1):
        print(" ",end=" ")
    for j in range(x+1):
        print("*",end=" ")
    print()
      

5.HALLOW RECTANGLE
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


6.HALLOW RIGHTANGLE TRIANGLE
n=int(input())
for i in range(n):
    for j in range(i+1):
        if i==n-1 or j==0 or i==j:
            print("*" ,end=" ")
        else: 
            print(" " ,end=" ")
    print()



