# q = 0
# for x in range(1,101):
#     if x % 3 == 0:
#         q+=x
# print("Fizz")


for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
        
        
        
## WRONG WAY TO CODE IT    
# for x in range(1,101):
#     if x % 3 == 0:
#         print("Fizz")
#     elif x % 5 == 0:
#         print("Buzz")
#     elif x % 3 == 0 and x % 5 == 0:
#         print("FizzBuzz")
#     else:
#         print(x)