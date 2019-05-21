import json
from difflib import get_close_matches

data = json.load(open("data.json"))
word = input("Enter your word:").lower()

if word in data.keys():
    print("\n".join(data[word]))
    
elif len(get_close_matches(word, data.keys(), cutoff=0.8))>0:
    yn = input("Did you mean %s [Y/N]?" % get_close_matches(word, data.keys())[0]).lower()
    if yn in ["y", "yes"]:
        print("\n".join(data[get_close_matches(word, data.keys())[0]]))
    elif yn in ["n", "no"]:
        print("%s is not a real word" % word)
    else:
        print("%s is not a valid entry" % yn)
else:
    print("This is not a real word")


    