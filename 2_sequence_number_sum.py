# 4321=>4+3+2+1=>10

def sum_of_sequence(n):
    if len(str(n))==1:
        return n
    # int we have to write
    return (n%10 + sum_of_sequence(int(n/10)))
print(sum_of_sequence(4321))