print("Welcome to the rollercoaster of 'Death'!")
height = int(input("What is your height in cm? "))
if height > 121:
  print("Youre big guy")
elif height == 119:
  print("Take your sit")
else:
  print("Come when youre taller")
####################################
height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))
bill = 0
if height > 121:
  print("Youre big guy")
  if age < 12:
    print("Fee is 5$")
    bill = 5
  elif age <= 18:
    print("Fee is 7$")
    bill = 7
  elif age <= 45:
    print("Fee is 12$")
    bill = 12
  elif age >= 45 and age <= 55:
    print("Ride is free!")
  else:
    print("Sorry youre too old")
  photo = input("Do you want a photo? Y or N? ")
  if photo == "Y":
    bill+=3
    print(f"You total fee is ${bill}")
  if photo == "N":
      print(f"You total fee is ${bill}")
else:
  print("Come when youre taller")

#########################################

  
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

#####################
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
else:
    print("Not leap year.")
    
    
###############################################################


# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
cost = 0
if size == "S":
  cost = 15
elif size == "M":
    cost = 20
elif size == "L":
    cost = 25
if add_pepperoni == "Y":
  if size == "S":
    cost += 2
  else:
    cost += 3
if extra_cheese == "Y":
  cost += 1
  
print(f"Your final bill is: ${cost}")






# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

N1=name1.lower()

N2=name2.lower()

#combine names together

TL=N1+N2

#counting letters in names

T=int(TL.count("t"))

R=int(TL.count("r"))

U=int(TL.count("u"))

E=int(TL.count("e"))

s=T+R+U+E

L=int(TL.count("l"))

O=int(TL.count("o"))

V=int(TL.count("v"))

E=int(TL.count("e"))

#counting next Step

u=L+O+V+E

#conditions

if s<0 and u<10 or s>8 and u>=0:

  print(f"Your love score is {s}{u}%, you go together like coke and mentos")

elif s>=4 and u>=0 or s<=5 and u<=0:

  print(f"Your score is {s}{u}%, you are alright together")

else: print(f"Your score is {s}{u}%")

####################################################

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
l_o_r = input("Where do you want to go? Left or Right?")
if l_o_r == "Left":
  nxt = input("Now you in the cave with water.What to do now? Swim or Wait?")
else:
  print("You have parished")
if nxt == "Swim":
  nxt_2 = input("In front of you now 3 doors.Which one will you open?Red,Green or Blue?")
else:
  print("You have parished")
if nxt_2 == "Green":
  print("You have escaped with ship full of treasures!")
elif nxt_2 == "Red":
  print("You were set ablaze")
elif nxt_2 == "Blue":
  print("You drowned")
else:
  print("Game Over! You met your final death.")
