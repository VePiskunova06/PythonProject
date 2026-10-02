#11.
best = 0

while True:
    score = int(input())
    if score == -1:
        break
    if score > best:
        best = score

print(best)