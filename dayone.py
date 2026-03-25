import math
import random
print("SQUARE ROOT",math.sqrt(625))
print("FACTORIAL",math.factorial(6))
print("FLOOR VALUE",math.floor(4.7))
print("CEIL VALUE",math.ceil(4.7))
print("POWER",math.pow(5,3))
print("ABSOLUTE VALUE",math.fabs(-18))
print("RANDOM INTEGER",random.randint(1, 10))
print("RANDOM FLOAT",random.random())
print("RANDOM CHOICE",random.choice([10,20,30,40,50]))
r = [10,20,30,40,50]
random.shuffle(r)
print("RANDOM SHUFFLE",r)
print(r)
x=random.randint(2,21)
if(x%2==0):
    print(x,"is an even number")
#DATE TIME MODULE
import datetime
print(datetime.datetime.now())