
# sum_of_any_consecutive=(2N+ n-n**2)/2n

# 10=> 1+2+3+4

def sum_consecutive(N):
    
    n=2
    count=0
    
    #while 2*N + n* n**2 -> numerator is +ve
    while 2*N + n-n**2>0:
        # adding bracks is very very imp
        
        a=( 2*N +n - n**2)/(2*n)
        
        #if a is natural number , there is no float
        if a-int(a)==0:
            print(a,n)
            count+=1
        n+=1
    return count

print(sum_consecutive(10))  
        
        