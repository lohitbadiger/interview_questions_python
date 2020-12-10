# 0,1,1,2,3,5,8,13,21

# recrusive way 

def fib(n):
    if n==1 or n==0:
        return 1
    else:
        return fib(n-1)* fib(n-2)
print(fib(100))

print('------------------------------------')
    
# dynamic way
calculated={}

def fibonaci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    
    elif n in calculated:
        # to get till n number of fib
        # print(calculated[n])
        
        return calculated[n]
    else:
        calculated[n]=fibonaci(n-1)+fibonaci(n-2)
        return calculated[n]
print(fibonaci(10))
