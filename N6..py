#6.
N = int(input())
subscribers = 10
month = 1

while subscribers <= N:
    subscribers *= 2
    month += 1
print(month)