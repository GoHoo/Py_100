#my code
"""
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
rslt = round(weight / height ** 2)
if rslt < 18.5:
  print(f"Your BMI is {rslt}, you are underweight.")
elif rslt < 22:
  print(f"Your BMI is {rslt}, you have a normal weight.")
elif rslt < 28:
  print(f"Your BMI is {rslt}, you are slightly overweight.")
elif rslt < 33:
  print(f"Your BMI is {rslt}, you are obese.")
else:
  print(f"Your BMI is {rslt}, you are clinically obese.")
  """"


# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
