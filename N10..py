#10.
previous = float(input())
count = 0

while True:
    current = float(input())
    if current == 0:
        break
    if current < previous:
        count += 1
    previous = current

print(count)