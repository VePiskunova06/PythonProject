import math
#стороны
a = float(input())
b = float(input())
c = float(input())

A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))
B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2*a*c)))
C = math.degrees(math.acos((a**2 + b**2 - c**2) / (2*a*b)))

print(A)
print(B)
print(C)