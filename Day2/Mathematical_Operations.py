# print("My age: " + str(12))

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)
print(2 ** 4) #Exponents 
print( 6 // 2) #Removes decimal points. Divides and then removes decimals

# PEMDAS
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

weight = input("please enter your weight")
height = input("please input your height")

weight_number = int(weight)

height_number = int(height)

heightM = height_number / 100

new_bmi = weight_number // ( heightM * heightM)

bmi_string = str(new_bmi)

print("Your BMI is " + bmi_string)