s = input()
start, finish = s.split("-")

x1 = "abcdefgh".index(start[0])
y1 = int(start[1])

x2 = "abcdefgh".index(finish[0])
y2 = int(finish[1])

if (abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or (abs(x1 - x2) == 2 and abs(y1 - y2) == 1):
    print("верно")
else:
    print("ошибка")