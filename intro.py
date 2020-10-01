
#Functions go on top of the file
def test():
    print("I'm a function")

def separator():
    print("-----------")


print('Hello')  #There are no semi-colons

# Declaring Variable types:
name = 'Ingrid'
last = 'Davis'
age = 30
found = False
total = 33.44
products = [] #an array is called a list

print (name)
print (name + " " + last) #string concatenation

print (age + age)
print (name + " is " + str(age) + " years old.")

separator() #calling the function from the top to here

# math operations
print (age - 10)
print ( age +26)
print (age *2)
print (age /2)
print (age % 2)

separator()

#if statements
if ( age < 80):
    print ('You are still young!')
elif(age ==80):
    print ('You are almost old') 
else:
    print('sorry, you are old :( ')
