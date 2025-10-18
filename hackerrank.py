# IF THE INPUT IS 5 PRINT 12345

def function(n):
    a = ""
    for i in range(1,n+1):
        a += str(i)
    print(a)
function(3)

# LIST COMPREHENSIONS
"""
x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
z = int(input("Enter number 3: "))
n = int(input("Enter the number : "))
list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(list)
"""

list = [x*x for x in range(5)]
print(list)

" using both if and else in list comprehensions"
print([x**2 if x % 2 == 0 else x**3 for x in range(1,6)])

a = [1,2,3,4,5,6,7,8,9]
print([i*i if i<5 else i for i in a])

first_name = input()
last_name = input()
def print_full_name(first, last):
    # Write your code here
    print("Hello "+ first_name + " " + last_name + "! " + "You just delved into python.")
print_full_name(first_name,last_name))



