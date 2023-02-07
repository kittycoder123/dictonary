import json
from difflib import get_close_matches
data=json.load(open("dictionary.json"))
def translate(w):
 w= w.lower()
 if w in data:
    return data[w]
 elif len(get_close_matches(w,data.keys()))>0:
    yn=input("did you mean % s instead? Enter Y if yes or N for no"%get_close_matches(w,data.keys())[0])   
    yn=yn.lower()
    if yn=="y":
      return data[get_close_matches(w,data.keys())[0]]   
    elif yn =="n":
        return "The word does't exist. Please double check it" 
    else:
        return "we did not understand your entry"
 else:
   return "the word does not exist. please double check it"

word=input("Enter word: ")
output=translate(word)  

if type(output)==list:
   for item in output:
      print (item)
else:
   print(output)

input("press ENTER to exit")
