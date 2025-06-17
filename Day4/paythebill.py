import random

#1st option
friends = ["Pranav", "Malhar", "Shardul", "Shubham", "Sumit"]
print(random.choice(friends)) #chooses a random element from a list

#2nd Option
random_index = random.randint(0, 4)
print(friends[random_index]) 
