#11.
xc = int(input("xc = "))
yc = int(input("yc = "))
r = int(input("r = "))
x = int(input("x = "))
y = int(input("y = "))

d = (x - xc) ** 2 + (y - yc) ** 2

if d < r ** 2:
    print("Точка внутри окружности")
elif d == r ** 2:
    print("Точка лежит на окружности")
else:
    print("Точка вне окружности")