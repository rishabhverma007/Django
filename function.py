def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):    
    return a*b
def divide(a,b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a/b
print(add(5, 3))
print(subtract(5, 3))
print(multiply(5, 3))
print(divide(5, 3))  

#SQUARE AND CUBE
def square(x):
    return x**2
def cube(x):
    return x**3
print(square(4))
print(cube(4))