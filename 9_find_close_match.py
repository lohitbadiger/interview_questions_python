# Find all close matches of input string from a list
# ex
# difflib.get_close_matches(word, possibilities, n, cutoff) 

from difflib import get_close_matches

def close_match(word,possibalities):
    print(get_close_matches(word,possibalities,cutoff=.5, n=3))
    

close_match('Windozp',['Win','windo','window', 'winzip'])   