# write a program to print common letters betweeen 2 strings

''' ex:     'Raina' and 'Rany'
    o/p =>  'R','a'  '''
    
    
def common():
    
    string1=input('enter first string')
    string2=input('enter second string')
    
    str1=set(string1)
    str2=set(string2)
    
    common= str1 & str2
    print(common)
common()      