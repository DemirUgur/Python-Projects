import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translator(w):
    if w in data.keys():
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        word = get_close_matches(w,data.keys())[0]
        yn = input("Did you mean %s? Press Y for yes and N for no\n" % word)
        if yn == 'y' or yn == 'Y':
            return data[word]
        else:
            return None 
    else:
        return "No word found\n"

word = None
while True:
    word = input("Enter a word: ")
    if word == '/end':
        break
    myLst = translator(word)
    if isinstance(myLst, list):
        for i in myLst:
            print(i)
    else:
        print(myLst)
    
