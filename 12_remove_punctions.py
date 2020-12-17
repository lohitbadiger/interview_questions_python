def no_pucn(string):
    
    punc='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in string:
        if x in punc:
            string=string.replace(x,'')
    print(string)

no_pucn('fgshadgjkl$%^&jhk^*&(')