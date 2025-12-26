1. you are given an array A of size N,where each element represents the number of 
cupcakes sold in a single transcation your task is to find  and return an integer
value representing the sum of the cupcakes from the transcations where 5 or more 
cupcakes where sold return 0 if there is no transaction with more than 5 cupcakes sold.

program:
    def cupcakes(N,arr):
        sum=0
        for i in range(N):
            if A[i]>=5:
                sum+=A[i]
            print(sum)
        N=5
        arr=[1,2,5,8,3,7,5]
        cupcakes(N,A)