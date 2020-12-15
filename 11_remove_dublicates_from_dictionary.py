
# Get Unique values from list of dictionary

print('--------1--------------------')
print()

def dict_unique(items):
    #using set +values +comprehension
    optput=list(set([i for item in items for i in item.values()]))
    print(optput)
    
items= [{'gfg' : 1, 'is' : 2},{'best' : 1, 'for' : 3}, {'CS' : 2}] 

dict_unique(items)    

print()
print()
print('-------2---Approch----------------')
print()

from itertools import chain

def dictionary_unique(list1):
    list1=list(set(chain.from_iterable([item.values() for item in list1])))
    
    print(list1)    
    
list1=[{'gfg' : 1, 'is' : 2},{'best' : 1, 'for' : 3}, {'CS' : 2}] 
dictionary_unique(list1)

print('-------3---Approch----------------')

from itertools import chain
test_list = [{'gfg' : 1, 'is' : 2}, {'best' : 1, 'for' : 3}, {'CS' : 2}] 

list1=chain.from_iterable(([i.values() for i in test_list]))
print(list(set(list1)))