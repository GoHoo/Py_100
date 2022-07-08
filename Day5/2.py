# 🚨 Don't change the code below 👇
from re import X


student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# print (min(student_scores))
# print (max(student_scores))
x = 0

for score in student_scores:
    if score > x:
        x = score 
print(f"The highest score in the class is: {x}")

h_val = student_scores[0]

for v in student_scores:
    if v > h_val:
        h_val = v
print(v)

ttl_score = sum(student_scores)
print()
nmb_students = len(student_scores)
h_scr = round(ttl_score / nmb_students)
print(f"The highest score in the class is: {h_scr}")
