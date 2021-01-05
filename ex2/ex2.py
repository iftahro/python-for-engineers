""" Exercise #2. Python for Engineers."""

#########################################
# Question 1 - do not delete this comment
#########################################
a = 3
lst = [1, 2, 3, 4, 5]

for i in range(len(lst)):
    if lst[i] % a == 0:
        print(i)
        break
else:
    print(-1)

#########################################
# Question 2 - do not delete this comment
#########################################
lst2 = ['hello', 'world', 'course', 'python', 'day']

total_avg = sum(map(len, lst2)) / len(lst)

# Write the code for question 2 using a for loop below here.
num = 0
for element in lst2:
    if len(element) > total_avg:
        num += 1
print(f"The number of strings longer than the average is: {num}")

# Write the code for question 2 using a while loop below here.
num = 0
i = 0
while i < len(lst2):
    if len(lst2[i]) > total_avg:
        num += 1
    i += 1
print(f"The number of strings longer than the average is: {num}")

#########################################
# Question 3 - do not delete this comment
#########################################

lst3 = [0, 1, 2, 3, 4]

s = 0
for i in range(len(lst3) - 1):
    s += lst3[i] * lst3[i + 1]
print(s)

#########################################
# Question 4 - do not delete this comment
#########################################

lst4 = [1, 2, 4, 6, 5, 9]

new_lst = lst4[:2]
for i in range(2, len(lst4)):
    if abs(lst4[i] - new_lst[-1]) > abs(new_lst[- 1] - new_lst[- 2]):
        new_lst.append(lst4[i])
print(new_lst)

#########################################
# Question 5 - do not delete this comment
#########################################

my_string = 'abaadddefggg'
k = 3

for i in range(len(my_string) - k + 1):
    if my_string[i: i + k] == my_string[i] * k:
        print(f"For length {k}, found the substring {my_string[i: i + k]}!")
        break
else:
    print(f"Didn't find a substring of length {k}")
