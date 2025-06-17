#Range function 

#example
# for number in range(1, 11): #prints uptill 10 does not include 11
#     print(number)

# for number in range(1, 11, 3): #the last digit tells the increment number.
#     print(number)

sum = 0
for number in range(1, 101):
    sum = sum  + number

print(sum)    

