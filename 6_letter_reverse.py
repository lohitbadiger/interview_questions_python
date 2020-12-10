# reverse strings letters
def reverse_letters(string):
    if len(string)==1:
        return string
    
    return reverse_letters(string[1:]) + (string[0])

# string=input('enter string')
string='lohit badiger'
print(reverse_letters(string))


print('----------------------------')

# def reverse_letter2(string):
#     string = "".join(reversed(string)) 
#     print(string)
# string='lohit badiger'
    
# reverse_letter2(string)

# print('----------------------------')


# def reverse_letetr(string):
#     string=string[::-1]
#     print(string)
# string='lohit badigers'
    
# reverse_letetr(string)