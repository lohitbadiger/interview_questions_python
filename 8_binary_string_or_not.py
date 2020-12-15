# write a program to check string contains 0 or 1  or 01 both

def check_binary(string):
    
    check={'0','1'}
    
    string=set(string)
    
    if check==string or string=={'1'} or string=={'0'}:
        print('Yes')
    else:
        print('No')
if __name__=='__main__':
    string='1010102'
    string2='10101010'
    
    check_binary(string)
    check_binary(string2)

print('-------------------------------------------')
print('iteration way')
 
def check_binary2(string):
    
    
    values='01'
    count=None
    for i in string:
        if i not in values:
            count=1
            break
      
    if count==1:
        print('No')
    else:
        print('Yes')
        
check_binary2('123')
