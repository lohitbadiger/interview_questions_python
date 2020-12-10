# given number is prime or not
def prime_num_or_not(n):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                print('given number is not prime')
                print(i,"times",n//i,"is",n)
                break
        else:
            print('given number is prime')
    else:
        print('given number is not prime')
# n=input('enter the number')
n=3
prime_num_or_not(n)