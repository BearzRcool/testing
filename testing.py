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
#figure out how to check if you win

images = ["💎","💎","💎","💎","💎","💎","💎","💎","💎"]


money = 100

def MainUI():
    mainUI = "| " + str(images[0]) + " | " + str(images[1]) + " | " + str(images[2]) +  " |\n| " + str(images[3]) + " | " + str(images[4]) + " | " + str(images[5]) + " |\n| " + str(images[6]) + " | " + str(images[7]) + " | " + str(images[8]) + " |"
    print (mainUI)
def RollSlots():
    global earnings
    earnings = 0
    Jackpot = random.randint(1,100)
    print (Jackpot)
    if Jackpot == 1:
            for i in range(len(images)):
                images[i] = '💎'
            print("GIANT JACKPOT!!")
    elif Jackpot == 2 or Jackpot == 3:
            for i in range(len(images)):
                images[i] = '🍀'
            print ("JACKPOT!!!")
        
    else:
        for i in range(len(images)):
            test = random.randint(1,102)
            #🍒|🍋|🍌|🍊|🍎|🍉|🍇|🍀|⛔|💎|💸|🎲|🥝|🍍|🍺|🍫|
            # MAKE THE THINGS MORE FAIR
            if test == 101 or test == 102 or test == 1 or test == 2 or test == 3 or test == 4 or test == 5 or test == 6 or test == 7:
                images[i] = "🍒"
            elif test == 8 or test == 9 or test == 10 or test == 11 or test == 12 or test == 14 or test == 15 or test == 16 or test == 17:
                images[i] = "🍋"
            elif test == 18 or test == 19 or test == 20 or test == 21 or test == 22 or test == 23 or test == 24 or test == 25 or test == 26:
                images[i] = "🍉"
            elif test == 27 or test == 28 or test == 29 or test == 30 or test == 31 or test == 32 or test == 33 or test == 34 or test == 35:
                images[i] = "🍊"
            elif test == 36 or test == 37 or test == 38 or test == 39 or test == 40 or test == 41 or test == 42 or test == 43 or test == 44:
                images[i] = "🍇"
            elif test == 45 or test == 46 or test == 47 or test == 48 or test == 49 or test == 50 or test == 51 or test == 52 or test == 53 or test == 54 or test == 55:
                images[i] = "🥝"
            elif test == 56 or test == 57 or test == 58 or test == 59 or test == 60 or test == 61 or test == 62 or test == 63 or test == 64 or test == 65 or test == 66 :
                images[i] = "🍍"
            elif test == 67 or test == 68 or test == 69 or test == 70 or test == 71 or test == 72 or test == 73 or test == 74 or test == 75:
                images[i] = "🎲"
            elif test == 76 or test == 78 or test == 79 or test == 80 or test == 81 or test == 82 or test == 83 or test == 84:
                images[i] = "🍺"
            elif test == 85 or test == 86 or test == 87 or test == 88 or test == 89 or test == 90 or test == 91 or test == 92:
                images[i] = "🍫"
            elif test == 93 or test == 94 or test == 95 or test == 96 or test == 97:
                images[i] = "🍀"
            elif test == 98 or test == 99 or test == 100:
                images[i] = "💎"
    

def Winnings():
    earnings = 0
        #  A B C    D E F    G H I 
    Win = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]]
    for win in Win:
        a, b, c = win
        #🍒|🍋|🍌|🍊|🍎|🍉|🍇|🍀|⛔|💎|💸|🎲|🥝|🍍|🍺|🍫|
        #ADD THE REST OF THE SYMBOLS EQUAL MONEY
        if images[a] == images[b] == images[c]:
            if images[a] == "🍒":
                earnings += 30
            elif images[a] == "🍋":
                earnings += 30
            elif images[a] == "🍉":
                earnings += 30
            elif images[a] == "🍀":
                earnings += 70
            elif images[a] == "💎":
                earnings += 150

    print("You won " + str(earnings) + '$!!!')
    return earnings

        
while True:
   
    question = input("Gamble? Costs 10$ You have " + str(money) + '$ ' )
    os.system('cls')
    
    if question == '':
        
        money -= 10
        RollSlots()
        MainUI()
        money += Winnings()
        

    
