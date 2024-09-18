# Create a function to check if a number is prime

def prime_no(x):
    if x<=1:
        return False
    if x==2 or x==3:
        return True
    if x%2==0 or x%3==0:
        return False

    i=5
    while i*i<=x:
        if x % i==0 or x % (i+2)==0:
            return False
        i+=6
    return True

res=10037
print(prime_no(res))


import math


# Write a script using the math module to calculate the area of a circle

def area_of_circle(radius):
    return math.pi*math.pow(radius,2)

radius=8
res=area_of_circle(radius)
print(f"The area of circle:{res:.2f}")
