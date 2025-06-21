# def greet():
#     print("Hello 1")
#     print("Hello 2")
#     print("Hello 3")

# greet()

# def name_greet(name): #this is called a parameter (name)
#     print(f"Hello your name is {name}")

# user_name = input("What is your name?")
# name_greet(user_name) #this is an argument. A piece of data passed in a function

#Funtions with more than one Input

def greet_with_location(name, location):
    print(f"Hello your name is: {name}")
    print(f"You live in: {location}")

# user_name = input("what is your name?")
# user_location = input("where do you live?") #arguments taken from user inputs
# greet_with_location(user_name, user_location)

greet_with_location("pranav", "Pune") #These are positional arguments.

#You can also use keyword arguments like 
greet_with_location(name = "pranav", location="Pune") #Define the arguments here