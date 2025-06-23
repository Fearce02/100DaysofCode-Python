#what are dictionaries?
#dictionaries in python are similar to Objects. the data is stored in key value pairs.

#Creating a dictionary.

#{KEY: VALUE} this is the syntax for it
#make sure you define the data type clearly in keys. Example - "" for strings. 123 for numbers. true or false for booleans.

dictionary = {
    "Bug" : "An error in a program that prevents the program from running as expected",
    "Function": "A block of code that performs a certain action and can be easily called again and again",
    "Loop" : "A block of code that performs a certain action again and again until a condition is met"
}

print(dictionary) #prints the above dictionary.
print(dictionary["Bug"]) #prints the value of the "KEY" provided in the square brackets.
print(dictionary["Loop"])

#adding a new key in an existing dictionary.
dictionary["New"] = "This is a new key"
print(dictionary)

#you can also create an empty dictionary.
empty = {}
empty["hello"] = "hello world"
print(empty)

#Wiping an existing dictionary
# dictionary = {} #deletes the data in it.
# print(dictionary)

# Edit an item in the dictionary.
empty["hello"] = "Hello this is the new python program"
print(empty)

#looping through a dictionary.
for key in dictionary:
    print(key) #prints just the key
    print(dictionary[key]) #prints the value of the keys