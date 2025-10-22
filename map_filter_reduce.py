l  = [1,2,3,4,5,6,7,8,9,10]

def square(n):                     #for map
    return n*n

def comparison(n):                 #for filter 
    if n>=5 and n<=7:              #functions used in filter return either True or False
        return True
    else:
        return False 

m = list(map(square, l))
f = list(filter(comparison,l))

print(m)
print(f)

from functools import reduce          #before using reduce we have to import this

# def product(a,b,c):
#     return a*b*c

def sum(a,b):
    return a+b

# r_p = list(reduce(product, l))
r_s = reduce(sum , l)

# print(r_p)        this will throw an error and will say that one positional argument is missing
print(r_s)


def product(a,b):
    return a*b

r_p_1 = (reduce(product, l))
print(r_p_1)

