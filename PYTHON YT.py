print("hello world")
print('''how are you
i am fine''')
character_name = "Rahul"
character_age = "35" #we can't use int here because we are concatinating it with string and
# we can't concatinate string with int
print(character_name + " is a very intelligent boy")
print(character_name + " is " + character_age + " years old.") 
print(character_name + " " + character_age)
print("ABHISHEK\nSHAHI")
print("ABHISHEK\tSHAHI")
print("\"Abhishek\" Shahi !")
a = 5
b = "0"
print(a)
print(b)
print(type(a))
print(type(b))
a = "ABHISHEK shahi"
print(a.lower())
print(a.upper())
print(a.swapcase())
print(a.isupper())
print(a.islower())
print(str(5))
print(int("5"))
a = 948
print(float(a))
print(str(a))
a = "GIRAFFE ACADEMY" 
print(a.lower().islower())
print(a.lower().isupper())
print(len(a))
print(a[0])
print(a[0::2])
print(a.index(" "))
print(a.replace(" ", "+"))
print(9+5893058353.353353)
a = 19
b = 9 
print(a % b) #a % b means remainder when a is divided by b
a = 5
print("Rahul's \"age\" is " + str(a))
print(10/3)
print(10//3)
print(10**3)
print(10%3)
my_num = -5
print(abs(my_num))
print(pow(3,2)) #3^2
print(max(3,6)) #6>3
print(min(3,6)) #3<6 
print(pow(4,90))
print(4**90) 
print(round(3.909404)) 
print(float(4.99))
print(round(3.5))


from math import *
print(floor(3.99)) #it will convert 3.99 to 3
print(ceil(4.01)) #it will convert 4.01 to 5
print(sqrt(2)) #it will give square root of 2 which is 1.4142135623730951



# lists 
friends = ["ABHISHEK" , "ANKIT" , "SHIVAM" , "LAKSHAY" , "YASH" , "KUSH"]
print(friends)
print(friends[4])
print(friends[-1]) 
print(friends[-1::-1]) 
print(friends[0:3]) 
print(friends[0:3:2]) 
friends[3] = "AMAN"
print(friends)
numbers = [1,2,3,4,5,6,7,8,9,10]
friends.extend(numbers) #it will add numbers list to friends list
print(friends)
friends.append("DEVANSH")



print(friends)
'''friends.clear()          #it will clear the whole list
print(friends) '''
friends.pop() #it will remove the last element of the list
print(friends) 
print(friends.index("ABHISHEK"))
print(friends.index("ANKIT"))
add_on = ["RAM", "RAM", "RAM"]
friends.extend(add_on)
print(friends)
print(friends.index("RAM"))
print(friends.count("RAM"))
list = [1,2,3,4,5,6,7,8,9,10, -1, -9384] #arranges it in ascending order
list.sort()
print(list)
list.reverse() # reverses the list
print(list)
abcd = [1,2,3,4,5,6,903452]
abcd_=abcd.copy() # copies the list
print(abcd_)


#TUPPLES
coordinates = (4,5)
print(coordinates)
print(coordinates[0])
print(coordinates[1])

'''coordinates[1] = 9
print(coordinates)      # tuples are immutable unlike strings so they can't be changed
''' 




#FUNCTIONS
#rules for naming function - name should be written completely in lower case 
#                            when we are writing 2 or more than 2 words we can put _ between the words

def say_hi():
    print("hello user")

say_hi()

def hello(name):
    print("Hello " + name)

hello("Abhishek")
hello("Akshay")


def hello(name, age):
    print("Hello " + name + "! You are " + age)

hello("Abhishek","17")
hello("Akshay","20")

# we can also do above eg by this way
def hello(name, age):
    print("Hello " + name + "! You are " + str(age) + '.')

hello("Abhishek",17)
hello("Akshay",20)

''' using return while defining function'''
def cube(x):
    return x**3
print(cube(2))

def quadratic_equation(a,b,c):
    return (-b+(b**2-4*a*c)**0.5)/(2*a), (-b-(b**2-4*a*c)**0.5)/(2*a)
print(quadratic_equation(1,-2,1))





def square_function(b):
    return b*b
result = square_function(16)
print(result)


def square_function(b):
    return b*b
print(square_function(90))


#if and else statements with and/or. Don't write anything in front of else not even any condition
# just write else: thats it  

is_male = True
if is_male:
    print("I AM A MALE")



is_male = False
if is_male:
    print("I AM A MALE") #it won't print anything bcz the condition is wrong


is_male = True
if is_male:
    print("I AM A MALE") 
else:
     print("I AM NOT A MALE")

is_male = False
if is_male:
    print("I AM A MALE") 
else:
     print("I AM NOT A MALE")


tall = True

if not tall:
    print("You are beautiful")
else:
    print("You are ugly")


tall = True

if tall:
    print("You are beautiful")
else:
    print("You are ugly")



genious = True
good_looking = True
if genious and good_looking:
    print("Ypu are handsome")
else:
    print("You are not handsome")


short = True
good_looking = True
genious = True
if not short and genious and good_looking:
    print("You are bad")
elif short and not good_looking:
    print("You are good")
else:
    print("You are the best") #1.if - if statement is right then it will be printed.
                              #2.if - if statement is wrong then if elif is right it will be printed 
                              #3. otw else statement will be printed
                            #   we can create infinte elif conditions


# defining functions using if and else and elif (else if)


def max(x,y,z):
    if x>y and x>z:
        print(x)
    elif y>z and y>x:
        print(y)
    elif z>x and z>y: 
        print(z)
max(45,90,1)



def max(x,y,z):
    if x>y and x>z:
        print(x)
    elif y>z and y>x:
        print(y)
    elif z>x and z>y: 
        print(z)
print(max(43,950,531)) #it is giving 90 and none both as outputs bcz in print there is no variable its empty
# we need not to write print jsut write max as in above code





# another way of finding max of 3 numbers
def max(x,y,z):          
    if x>y and x>z:
        return x
    elif y>z and y>x:
        return y
    else:
        return z
print(max(44,89,0))


# building a calculator using if and else and elif
""" remember the usage of = and ==  and float infront of input function bcz we can't do
arithmetical operations on strings we need to convert it into float not int bcz its a calculator"""
"""
a = float(input("Enter number 1: "))
z = input("Enter the operator: ")
b = float(input("Enter number 2: "))
if z == "+":
    print(a+b)
elif z == "-":
    print(a-b)
elif z == "*":
    print(a*b)
elif z == "/":
    print(a/b)
else:
    print("this operator can't be used")
"""
"""we can avoid this line of code but it will give error if we use other
                                  then these four ops so to tell the user we are using else """ 
    

# replacing words or shortforms to longforms (Dictionary)

dictionary= {"Mon":"Monday",          #use curly brackets and place commas correctly
             "Tue":"Tuesday",
             "Wed":"Wednesday",
             "Thu":"Thursday",
             "Fri":"Friday",
             "Sat":"Saturday",
             "Sun":"Sunday"}
print(dictionary["Sun"])          #1st method
print(dictionary.get("Mon"))      #2nd method 
print(dictionary.get("Hello","xyz"))   
# print(dictionary["Hello"])      #HERE WE ARE GETTING ERROR BUT WE WONT GET ERROR IF WE ARE USING GET


"""WHILE LOOPS"""
a = 2 
while a<=100:
    print(a)
    a = a**2
print("Square series")



a = 1
while a<=60:
    print(a)
    a = a*2
print("G.P with r = 2 and a = 1")

a = 1 
while a<=100:
    print(a)
    a = a + 30
print("A.P with a = 1 and d = 30")

#by this way we can create any series using while loop

z = 5
while z>1.3:
    print(z)
    z = z ** 0.5
print("Underoot series")
'''
# Building a guessing game 
guess_name = "Abhishek"
guess = ""
print("HINT -> MY NAME STARTS WITH A")
while guess != guess_name:
    guess = input("Enter your guessed name: ")
print("Congrats! You won.")
'''
     
# => READING FILES

# r means read that is we are just accessing the data of the file
# w means write that is we are overwriting the whole file
# r+ means read & write 
# a means append that is we are appending information to the existing file without overwritng.
'''
data = open("pytxt.txt", "r")
if data.readable() == True:    #or write if data.readable():
    print(data.read())
else:
    print("This file is not readable!")
data.close()

print("Another way to print this command")

with open("pytxt.txt", "r") as data:
    if data.readable():
        print(data.read())
    else:
        print("This file is not readable!")
print("Break")
data = open("pytxt.txt", "r")
print(data.readline())    #prints the first line if we do it n times then it will print n lines of the txt file
print(data.readlines())  # it prints all the lines of the txt file and combines all the lines of the txt file in a list.
# we also have to close the file by using
data.close()

data = open("pytxt.txt", "a")
data.write("\nI am currently pursuing B.TECH in CSE.")
data.close()  # by this code we are appending this line in the txt file.


data = open("pytxt.txt", "w")
data.write("This is the new file!")
data.close() #by this code we are rewriting the information of the whole file.'''

# Creating a new file

'''
new_file = open("pytxt.txt_1", "w")
new_file.write("Hello guys this is a new file created using python functions.")
new_file.close()

print("We are done with the reading and writing of the files.")'''

# CREATING OBJECT CLASSES


from yt_classes import data
student1 = data("Abhishek", 17, "1st", 8)
student2 = data("Akshay", 20, "3rd", 7.5)
student3 = data("Aman", 17, "1st", 3)

print(student1.cgpa)
print(student2.name)
print(student3.college_year)
print(student1.age)


print("pause")

from yt_classes import data
Abhishek = data("Abhishek", 17, "1st", 8)
Akshay = data("Akshay", 20, "3rd", 7.5)
Aman = data("Aman", 17, "1st", 3)

print(Abhishek.cgpa)
print(Akshay.name)
print(Abhishek.age)
print(Aman.college_year)

print(Abhishek.is_a_good_student())
print(Akshay.is_a_good_student())
print(Aman.is_a_good_student())

# TRANSLATOR AND FORMING MCQ QUESTIONS ARE STILL NOT DONE FROM FREE CODE CAMP (YT).

# RECURSIONS 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5)) 

# RECURSIONS FINISH
class employee:
    salary = 1200000           #THESE ARE CLASS ATTRIBUTES.
    language = "English"
    gender = "Male"

Abhishek = employee()
Abhishek.name = "Abhishek"   #THIS IS AN INSTANCE OR OBJECT ATTRIBUTE.
Akshay.name = "Akshay"
Akshay = employee()
print(Abhishek.name,Abhishek.gender,Abhishek.salary,Abhishek.language)
print(Abhishek.gender)
print(Abhishek.salary)
print(Abhishek.language)
print(Akshay.gender)

class students:
    standard = "12th"
    age = 16       #THIS IS A CLASS ATTRIBUTE
Akash = students()
Akash.age = 17     #THIS IS AN OBJECT/INSTANCE ATTRIBUTE
print(Akash.age,Akash.standard)      #bcz instance atributes are preferred over class attributes


# PASS BREAK AND CONTINUE IN PYTHON 

""" BREAK - USED TO TERMINATE THE LOOP ENTIRELY
    PASS - DOES NOTHING , ACTS AS A PLACEHOLDER
    CONTINUE - SKIPS TO THE NEXT ITERATION OF THE LOOP
"""
