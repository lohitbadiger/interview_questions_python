def word_reverse(words):
   words=words.split(' ')
   
   words=' '.join(reversed(words))
   
   print(words)

word_reverse('words are')
   
   
   
print('-------------------------------------')


def words_revers(words):
    
    for i in words.split()[::-1]:
        print (i,end=' ')
words_revers('words are')

# word reverse

def words(s):
    i=0
    words=[]
    spaces=[' ']
    length=len(s)
    while i<length:
        
        if s[i] not in spaces:
            word_start=i

            while i<length and s[i] not in spaces:
                i+=1
            words.append(s[word_start:i])
        i+=1
    return words
print(words('rango mongo'))