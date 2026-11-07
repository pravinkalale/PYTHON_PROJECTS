# 1 import the random module
import random

# 2 create subjects
subjects = [
    "A Lazy Software Developer",
    "A Chai Addict",
    "A Confused AI Robot",
    "A Wedding Photographer",
    "A Jobless Engineer",
    "A Sleepy Student",
    "A Talking Cow",
    "A Rich Beggar",
    "A Dancing Alien",
    "A Foodie Programmer",
    "A Village Sarpanch",
    "A Strict College Principal",
    "A Secret Agent",
    "A Hungry Dinosaur",
    "A Professional Procrastinator",
    "A Gym Trainer",
    "A Bollywood Villain",
    "A Delivery Boy",
    "A Python Developer",
    "A Cricket Fan",
    "A Ghost from Pune",
    "A Traffic Police Officer",
    "A Maggi Lover",
    "A Millionaire Auto Driver",
    "A Genius Monkey"
]

actions = [
    "starts dancing with",
    "challenges to a cricket match",
    "teaches Python to",
    "steals 100 samosas from",
    "declares war against",
    "runs away from",
    "secretly marries",
    "starts a fight with",
    "orders 500 pizzas for",
    "starts singing in front of",
    "challenges to a dance battle",
    "starts teaching mathematics to",
    "opens a tea stall for",
    "hacks the computer of",
    "sells vegetables to",
    "conducts a surprise mock test for",
    "starts arguing with",
    "proposes marriage to",
    "starts a YouTube channel with",
    "organizes a cricket tournament for",
    "starts a gym with",
    "forgets how to use a mobile phone",
    "starts cooking biryani for",
    "asks for a job at"

]

places_or_things = [
    "inside Pune Metro",
    "on the Moon",
    "inside Bigg Boss House",
    "at a village wedding",
    "inside a Python classroom",
    "during an IPL final",
    "at a railway station",
    "inside a haunted house",
    "at a five-star hotel",
    "inside a swimming pool",
    "at a vegetable market",
    "in a jungle",
    "inside a computer lab",
    "at a job interview",
    "inside a UFO",
    "at a police station",
    "on top of a moving bus",
    "inside a shopping mall",
    "at Fortune Cloud",
    "during a college lecture",
    "inside a marriage hall",
    "at a tea stall in Pune",
    "on the streets of Mumbai",
    "inside a cricket stadium",
    "at India Gate"
]

# 3 start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    
    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline) 
    
    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break
    
# print goodby message
print("\nThanks for using the Fake Headline Generator, Have a fun day!")
