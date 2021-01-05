''' Exercise #1 - solution. Python.'''

#########################################
# Question 1 - do not delete this comment
#########################################
S = 220.0
AB = 20.0
BC = 10.0
AD = 15.0
DC = 35.0

diameter = AB + BC + DC + AD
midsegment = (AB + DC) / 2
height = S / midsegment
print(f"Diameter is: {diameter}\n"
      f"Midsegment is: {midsegment}\n"
      f"Height is: {height}")

#########################################
# Question 2 - do not delete this comment
#########################################
my_name = "iftah"

print(f"Hello {my_name.capitalize()}!")

#########################################
# Question 3 - do not delete this comment
#########################################
number = '-17'
if int(number) % 7 == 0:
    print(f"I am {number} and I am an divisible by 7")
else:
    print(f"I am {number} and I am an not divisible by 7")

#########################################
# Question 4 - do not delete this comment
#########################################
text = 'oxana'
copies = 3

new_str = text[1::2] + text[::2]
print(new_str * copies)

#########################################
# Question 5 - do not delete this comment
#########################################
name = "droLtromedloV"
q = 4

if not name or q < 0 or q > len(name):
    print("Error: illegal input!")
else:
    sub1 = name[:q][::-1]
    sub2 = name[q:][::-1]
    print(f"{sub1} {sub2}")
