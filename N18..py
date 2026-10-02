#18.
x = int(input())

count = 0
for a in range(1, int(x ** 0.5) + 1):
    for b in range(a, int(x ** 0.5) + 1):
        if a * a + b * b == x:
            count += 1
print(count)