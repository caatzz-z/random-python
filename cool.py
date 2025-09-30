import random
theme = (input("Enter a theme for some cool phrases! :")).strip().lower()

if theme == "cool":
    phrases = [
        "omg so cool!",
        "OMMGGGG SO COOL!!!",
        "This is the coolest thing ever!!!"
    ]
    print(random.choice(phrases))
elif theme == "boi":
    phrases = [
        "ts so tuff boi",
        "hey boi",
        "yo ho ho boi"
   ]
    print(random.choice(phrases))
elif theme == "brah":
    phrases = [
        "brruuhhh",
        "braaaahhhhh",
        "beuyh"
    ]
    print(random.choice(phrases))
else:
    print("cool phrases coming soon...!!!!!!!!!")