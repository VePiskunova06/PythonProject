file = open("input.txt", "r", encoding="utf-8")
result = open("output.txt", "w", encoding="utf-8")

today = file.readline().strip()
n = int(file.readline())

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = int(today[:2])
month = int(today[3:])

today_number = sum(months[:month - 1]) + day
for i in range(n):
    line = file.readline().split()
    number = line[0]
    date = line[1]

    day = int(date[:2])
    month = int(date[3:])
    date_number = sum(months[:month - 1]) + day

    if today_number - date_number > 3:
        result.write(number + "\n")
file.close()
result.close()
