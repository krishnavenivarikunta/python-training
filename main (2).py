you are given two strings A and B.your task is to find and return a strings
represents the leftover string in A after removing all the letters that exists
in string B ,return "empty" if the output does not contain any value.

program:
    def leftover(a,b):
        left=" "
        remove=set(b)
        for ch in a:
            if ch not in remove:
                left+=ch
        if left:
            print(left)
        else:
            print("empty")
    a="ABCDEF"
    b="BDE"
    leftover(a,b)
    
        