# Build an interactive dictionary
# ********************************

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def findWord(w):

    w = w.lower()
    if w in data.keys():
        return data[w]
    elif w.title() in data.keys():
        return data[w.title()]
    elif w.upper() in data.keys():
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
       y_n = input("Do you mean %s instead. Enter Y if yes or N if no: " % get_close_matches(w,data.keys())[0])
       if y_n.upper() == 'Y':
           return data[get_close_matches(w,data.keys())[0]]
       elif y_n.upper() == 'N':
           return "Sorry! we don't have the word in our dictionary, please double check it."
       else:
           return "please check your query again."
    else:
       return "Sorry! we don't have the word in our dictionary, please double check it."


w = input("Enter a word to search: ")

output = findWord(w)

if type(output) == list:
    for item in output:
        print (item)
else:
    print (output)

