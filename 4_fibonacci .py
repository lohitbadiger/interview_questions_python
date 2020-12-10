# 0,1,1,2,3,5,8,13,21

calculated={}

def fibonaci(n):
    
    if n==0:
        return 0
    
    elif n==1:
        return 1
    
    elif n in calculated:
        return calculated[n]
    
    else:
        calculated[n]=fibonaci(n-1)+fibonaci(n-2)
        return calculated[n]

print(fibonaci(10))
    