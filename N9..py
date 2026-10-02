#9.
N, K, R = map(int, input().split())
length = N
day = 1

while length < R:
    length *= 1 + K / 100
    day += 1
print(day)
