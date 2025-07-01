#What are namespaces? and scopes.
# A namespace is a container that holds a set of identifiers (names) and the objects they are associated with.
# A scope is a region of the code where a namespace is accessible.

name = "Pranav" #Global Scoped Variable

def printName(name):
    newName = "Shardul" #Local Scoped Variable
    print(f"Hello {name} !")

# printName(name=name)

game_level = 3
enemies = ["Skeleton", "Zombie", "Dragon"]

if game_level < 5:
    new_enemy = enemies[0] #blocks like while if statements they dont count as creating a local scope.

#Python is different from other languages like C++ or Java, where function is the only way to create a local scope.
## In Python, blocks like if, for, while, etc. do not create a new local scope.
## This means that variables defined in these blocks are accessible outside of them.
## This is why we can access new_enemy here, even though it was defined inside the if block.
## However, if we define a function inside the if block, it will create a new local scope.
## For example:
def create_enemy():
    new_enemy = "Goblin"  # This is a local variable within the function scope.
    return new_enemy

# Calling the function to create a new enemy
new_enemy = create_enemy()  # This will call the function and assign the returned value to new_enemy.
# Now we can print the new_enemy variable
# This will print the new_enemy variable defined in the if block.   
print(new_enemy)