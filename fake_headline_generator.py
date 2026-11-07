# 1 import the random module
import random

# 2 create subjects
subjects = [
    "Shahrukh khan",
    "Virat kohli",
    "Nirmala Sitaraman",
    "A Mumbai Gate",
    "A Group of Monkeys",
    "Prime minister Modi",
    "Auto Rickshow Driver from pune",
    "Prashant Sir",
    "Kajal Mam"
]

actions = [
    "Launches",
    "Cancels",
    "dance with me",
    "eats",
    "Declares war on",
    "orders",
    "celebrates",
    "conducting Mock Test",

]

places_or_things = [
    "at Red Fort",
    "in mumbai local train",
    "inside parliment",
    "during IPL Match",
    "at India Gate",
    "in Fortune cloud",
    "at Cravita Technology",
    "in Pune metro"
]

# 3 start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    
    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline) 
    
    user_input = input("\nDo you want another headline? (yes/no)".strip().lower())
    if user_input == "no":
        break
    
# print goodby message
print("\nThanks for using the Fake Headline Generator, Have a fun day!")
