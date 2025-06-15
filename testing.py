import os
import time
import random
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
"""
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

"""
# lambda functions- super small and has no name (anonymous)

# function that don't take up a lot of space
# used for testing, quick calculations, or when you need a function for a short time
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
# -can used as function in a function
# uses less memory

def myfunc(n):
    return lambda a: a + n
num = myfunc(5)

print(num(10))
"""
# lambda practice
#Problem: Sorting Employees by certain criteria

#You're given a list of dictionaries, where each dictionary represents an employee with their name, age, and salary.

#Write a lambda function called sort_employees that takes this list, and a string key, which can either be age or salaary. #
#The function needs to return a list of employees based on ascending order
'''
employees = [
    {"name":"Alice", "age":23, "salary": 83000},
    {"name":"John", "age":33, "salary": 80400},
    {"name":"Bob", "age":26, "salary": 100000},
    {"name":"Janise", "age":16, "salary": 82000},
    {"name":"Lumberg", "age":28, "salary": 80010},
    {"name":"Ron", "age":40, "salary": 83400},
    {"name":"Patrick", "age":36, "salary": 83400},
    {"name":"Tim", "age":31, "salary": 83400},
    {"name":"Anthony", "age":46, "salary": 83400},
]
def sort_employees(employees, key):
        keylist = []
        namelist =[]
        for i in range(len(employees)):
            for j in range(i+1, len(employees)):
                if employees[i][key] > employees[j][key]:
                     temp = employees[i]
                     employees[i] = employees[j]
                     employees[j] = temp
        answer = ""
        for i in range(len(employees)):
            keylist.append(employees[i][key])
            namelist.append(employees[i]["name"])
            answer += str(namelist[i]) + ' : ' + str(keylist[i]) + ', '
        return answer

def lambda_sort_employees(employees, key):
    keylist = []
    namelist =[]
    answer = ""
    employees.sort(key= lambda x : x[key])
    for i in range(len(employees)):
        keylist.append(employees[i][key])
        namelist.append(employees[i]["name"])
        answer += str(namelist[i]) + ' : ' + str(keylist[i]) + ', '
    return answer

os.system('cls')
sorted_values = input("Sort the employees based on their age or salary? ")
sorted_values = lambda_sort_employees(employees,str(sorted_values))
print (sorted_values)
'''
# inventory problem
# create an inventory that you can show where you can remove items, add items
'''
inventory = ["sword", "shield"]
def AddInv(item):
    inventory.append(str(item))
def RemoveInv(item):
    try:
        inventory.remove(str(item))
    except:
        print("You don't have that item")
def CheckInv():
    printout = ' | '
    for i in range(len(inventory)):
        printout += str(inventory[i]) + " | "
    print (printout)
while True:
    item = input("Whwat do you want to do with your inventory? (add, remove, check) ")
    if str(item.lower()) == "add":
        item = input("What do you want to add? ")
        os.system('cls')
        AddInv(item)
    elif str(item.lower()) =="remove":
        item = input("What do you want to remove? ")
        os.system('cls')
        RemoveInv(item)
    elif str(item.lower()) == "check":
        os.system('cls')
        print("this is your inventory")
        CheckInv()
'''
#slots game?
#text based, will show up in the terminal
images = [1,2,3,4,5,6,7,8,9]
def RollSlots():
    for i in range(len(images)):
        images[i] = random.randint(1,5)
def Winnings():
    earnings = 0
    Win = ["a","b","c"], ["d","e","f"], ["g","h","i"], ["a","d","g"], ["b","e","h"], ["c","f","i"],
    ["a","e","i"], ["c","e","g"],
    ['a','b','c','d','e','f','g','h','i']
    for i in range(0,9):
        pass
money = 100
while True:
    mainUI = "| " + str(images[0]) + " | " + str(images[1]) + " | " + str(images[2]) +  " |\n| " + str(images[3]) + " | " + str(images[4]) + " | " + str(images[5]) + " |\n| " + str(images[6]) + " | " + str(images[7]) + " | " + str(images[8]) + " |"
    RollSlots()
    print(mainUI)
    question = input("What do you want to do? You have "+ str(money) + "$. ")
    money -= 10
    Winnings()

    
