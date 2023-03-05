import time
import math

a = int(input("Enter the number a "))
b = int(input("Enter the number b "))

time.sleep(b / 1000)
print(f"Square root of {a} after {b} miliseconds is {math.sqrt(a)}")