#lists in python are similar to array data structure.

states_of_india = ["UP", "Rajasthan", "Maharashtra", "Karnataka", "tamil-nadu", "Kerela", "Odisha", "Telangana", "Andhra-Pradesh", "Madhya-Pradesh"]
print(states_of_india[-5])
states_of_india[5] = "Jharkhand" #adding an element to a specifiq position
print(states_of_india)

states_of_india.append("Arunachal-Pradesh") #Adding an element to the last position.
print(states_of_india[-1])

states_of_india.extend(["Kashmir", "Delhi", "Punjab"]) #extends the list 
print(states_of_india)