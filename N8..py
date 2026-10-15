#8.
file = open("input.txt", "r", encoding="utf-8")
result = open("output.txt", "w", encoding="utf-8")

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for days in months:
    total = 0
    for i in range(days):
        steps = int(file.readline())
        total = total + steps

    average = total / days
    result.write(str(average) + "\n")
file.close()
result.close()
