#letters reverse in strings 


def reverse_letters(string):
    if len(string)==1:
        return string
    
    return reverse_letters(string[1:]) + (string[0])

# string=input('enter string')
string='lohit badiger'
print(reverse_letters(string))


print('----------------------------')

def reverse_letter2(string):
    string = "".join(reversed(string)) 
    print(string)
string='lohit badiger'
    
reverse_letter2(string)

print('----------------------------')


def reverse_letetr(string):
    string=string[::-1]
    print(string)
string='lohit badigers'
    
reverse_letetr(string)

print('----------------------------')

def reverse_string(string):
    ss=''
    for s in string:
        s=s+ss
    print(ss)
reverse_string('im going')