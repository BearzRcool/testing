import os
import time
# excption == error

#exception handling == error handling

#try-cath statement: try ode out, catch any errors
'''
try:
    print(x)
except NameError:
    print("What is that variable?")
except:
    print("Wyd dude")
'''
'''
while True:
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        operator = input("add or subtract? ")
        if operator == "add":
            print(num1 + num2)
            
        elif operator == "subtract":
            print(num1-num2)
            
    except ValueError:
        print("you did not pick a number, try again")

    else:
        print("no errors")
        break
    finally: 
        print("its over")
'''
#raising exceptions
#Throw exceptions ccording to whatever conditions you want
'''
print("Welcome to the new Mcdonalds' ketchup ordering system")
print("--------------------------------------------------------------")
while True:
    try:
        number_of_ketchup = int(input("How many ketchup packets do you want? "))
        if number_of_ketchup >= 50:
            raise Exception("too many packets bud")
        

    except ValueError:
        print("Thats not a number")
    else:
        print("here is your " + str(number_of_ketchup) + " packets of ketchup")
        print("have a great day")
        break
    finally: 
        print("---------------------------------------------------------------")

'''
"""
# Safe Division Calculator
# You are tasked with writing a program that asks the user to enter two numbers and divide the first number by the second.
# Hoewever, users might make mistakes, like entering non-number values, or try dividing by zero.
# Your job is to find a way to use exception handling to handle these errors gracefully.
# Requirements:
# 1. Prompt the user to enter two numbers. Numerator and Denominator.
# 2. Try converting the inputs to integers and divide them.
# 3. If the user enters something that isnt a number, send a message "Invalid input... enter a number"
# 4. If the user enters a divide by zero issue, "Error: can't divide by zero"
# 5. Print result if the divison is safe
# 6. Always print "Operator Completed" at the end, NO MATTER what happens.
try:
    os.system('cls')
    top = int(input("Enter a number be divided: "))
    bottom = int(input("Enter a number to divide the previous number: "))
    answer = top/bottom
    print(answer)
except ValueError:
    print("Invalid input... enter a number")
except ZeroDivisionError:
    print("Error: can't divide by zero")
finally:
    print("Operator Completed")
"""
# Alphabet Typing Game
"""
while True:
    try:
        time1 = time.time()
        abc = input("Type the alphabet: ")
        if abc != "abcdefghijklmnopqrstuvwxyz":
            print("try again")
        else:
            time2 = time.time()
            print("You did it in " + str(time2 - time1) + " seconds")
            break
    finally:
        print ("abcdefghijklmnopqrstuvwxyz")
"""
# lambda functions- super small and has no namy (anonymous)

# can take in any number of parameters and arguments
# but can only have one expression / line of code
number1 = lambda a : a + 10
print(number1(5))

# Example of function and lambda function side-by-side
def add_numbers(a, b):
    return a + b 
add = lambda a, b: a + b
print(add_numbers(10, 10))
print(add(10,10))

# why use lambda functions?

def myfunc(n):
    return lambda a: a + n
num = myfunc(5)

print(num(10))