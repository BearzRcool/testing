import os
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

        
