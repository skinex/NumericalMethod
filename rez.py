from math import *

def func(x):
    return x - (sin(x) / 2) - 1

def g(x):
    return 1 + (sin(x) / 2)

def solve(a,b,e):
    x0 = a
    x1 = g(x0)
    
    while (abs(x1 - x0)) > e:
        x0 = x1
        x1 = g(x0)
        
    lst = list()
    lst.append(x1)
    lst.append(func(x1))
    return tuple(lst)
    
a = float(input("a = "))
b = float(input("b = "))
e = float(input("e = "))

rez = solve(a,b,e)

print(rez)
