import json
from difflib import get_close_matches
  
# Loading data from json file
# in python dictionary
data = json.load(open("data.json"))
a="null"  
def translate(w):
    # converts to lower case
    w = w.lower()
  
    if w in data:
        return data[w]
    # for getting close matches of word
    elif len(get_close_matches(w, data.keys())) > 0:             
        yn = input("Did you mean % s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
  
# Driver code
print("Welcome To English Dictionary \n")
word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
a=input("\n Enter y to continue or n to exit")

if a=="y" :
      word = input("Enter word: ")
      for item in output:
        print(item)
      a=input("Enter y to continue or n to exit")
'''else:
    print(output)
input('Press ENTER to exit') '''
