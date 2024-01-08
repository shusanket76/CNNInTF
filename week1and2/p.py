import random
import os

a = [1,2,3,4,5,6,7]

per = 50

per = per *len(a)//100
array1 = random.sample(a, per)
print(a)
print(array1)