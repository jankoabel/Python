from math import sqrt

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

discriminant = b**2 - 4*a*c
x1 = (-b + sqrt(discriminant)) / (2*a)
x2 = (-b - sqrt(discriminant)) / (2*a)
print(f"The roots are {x1} and {x2}")
