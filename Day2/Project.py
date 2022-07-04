'''
print("Welcome to tip calculator")
bill = float(input("Total bill? $"))
tip = int(input("How much to tip? $ "))
ppl = int(input("How many people? "))

tip_i = tip / 100
fnl_pay = round((bill // ppl) * tip_i,2)
print(f"Each person should pay: ${fnl_pay}")    '''

"""
##  Problematic part was math as always , not the coding ability 
print("Welcome to tip calculator")
bill = float(input("Total bill? $ "))
tip = int(input("How much to tip? $ "))
ppl = int(input("How many people? "))

tip_i = (tip / 100) * bill
bill_tip = bill + tip_i
splitbill = bill_tip / ppl
fnl_pay = "{:.2f}".format(round(splitbill,2))
print(f"Each person should pay: ${fnl_pay}")    
"""

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

#long form
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

#If you want the final_amount to always have 2 decimal places.
#e.g. $12 becomes $12.00
#You can use this link to figure out how to do this:
#https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python
#This is how you can implement it:
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")
