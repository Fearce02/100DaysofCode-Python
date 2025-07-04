import random

def myFunc():
    for i in range(1, 20):
        if i == 20:
            print ("You got it!")
        

myFunc()

#the loop is checking for i  == 20, it never reacher 20 because range is set from (1, 20) which means it will go up to only 19.
# To fix this, we can change the range to (1, 21) or simply remove the condition.
#this is how you debug

#Reproducing a bug.

dice_images = [1, 2, 3, 4, 5, 6]
dice_nums = random.randint(1,6)
print(dice_images[dice_nums])

#the above code will throw an list index out of range error. But only sometimes
#to be specifiq it occurs only when the dice num is 6. because list index starts from 0 and goes up to 5.

