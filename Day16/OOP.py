#How to use Objects and Classes

#2 important things that make up an Object in Python are Its attributes and its methods.
#Attribute is just a word for a variable that is associated with a modeled object.
#Method is just a function that a particular modeled object can do. These are not free floating functions.

#In OOP we call a Blueprint of a object a Class.
#example. If we have 2 waiters named Betty and Henry. Both are objects which have same functions.

#Creating a Class.

import turtle
#can also write "from turtle import Turtle"

timmy = turtle.Turtle() #This is an object of the Turtle() class.
#timmy is an Object Turtle is a Class which we used to create the object.
print(timmy) #This will print the memory address of the object.
timmy.shape("turtle") #This will change the shape of the turtle to a turtle.
timmy.color("green") #This will change the color of the turtle to coral.\
timmy.forward(100) #This will move the turtle forward by 100 units.
timmy.right(90) #This will turn the turtle right by 90 degrees.
timmy.forward(100) #This will move the turtle forward by 100 units.
timmy.right(90) #This will turn the turtle left by 90 degrees.
timmy.forward(100) #This will move the turtle forward by 100 units.
timmy.right(90) #This will turn the turtle right by 90 degrees.
timmy.forward(100) #This will move the turtle forward by 100 units.
#This is how we create a a square using the turtle module.

#Attributes of an Object.
my_screen = turtle.Screen() #This is another object of the Screen() class.
print(my_screen.canvheight) #This will print the height of the screen. 

#Object Methods.
my_screen.exitonclick() #This will close the screen when clicked.

