
#functions

def print_menu():
    print ( "-" *15)
    print ( " Python Calc ")
    print ( "-" *15)

    print (" [1] Add")
    print (" [2] Subtract")
    print (" [3] Multiply")
    print (" [4] Division")

    print (" [5] My Age")

    """
    HOMEWORK:
    
    opc = 5
    ask for the year of birth
    tell the age
    """

    print('[X] Close')


#instructions

opc = ""
while( opc != 'X'):
    print_menu()
    opc = input ("Please choose an option: ") # ask user to choose option

    if(opc != 'X'):
        num1 = input("First number: ")
        num2 = input("Second number: ")

    if (opc == "1"):
        res = float(num1) + float(num2)
        print("Result " +  str(res))

    elif(opc == "2"):
        res = float(num1) - float(num2)
        print("Result " +  str(res))

    elif(opc == "3"):
        res = float(num1) * float(num2)
        print("Result " +  str(res))

    elif(opc == "4"):
        if (num2 == '0'):
            print ("Can not divide by 0, please enter a number greater than 0")
        else:
            res = float(num1) / float(num2)
            print("Result " +  str(res))


print ("Good-bye!")

"""
    After changes 
    - type a message
    - commit
    - push to send to GitHub
"""