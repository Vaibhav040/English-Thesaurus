import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]    
    elif get_close_matches(word, data.keys()):
        yn = input("Did you mean %s ? Enter Y if yes or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn =="N":
            return "The word doesn't exist. Please doule check it"
        else:
            return "we didn't understand your entry" 
    else:
        return "The word doesn't exist. Please double check it"

word = input("Enter the word: ")

result = translate(word)

if type(result) == list:
    for items in result:
        print(items)
else:
    print(result)        