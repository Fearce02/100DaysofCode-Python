student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_score = sum(student_scores) #sum function
# print(total_score)

#making your own sum function with for loop
# sum = 0
# for score in student_scores:
#     sum += score

# print(sum)   
# print(max(student_scores)) #prints the largest number from the list

largest_num = 0
for score in student_scores:
    if score > largest_num:
        largest_num = score

print(largest_num)