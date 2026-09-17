#11.
import math

r1 = float(input())
r2 = float(input())

r_outer = max(r1, r2)
r_inner = min(r1, r2)

area = math.pi * (r_outer**2 - r_inner**2)
print(area)