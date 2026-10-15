#7.
file = open("input.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()

file = open("input.txt", "w", encoding="utf-8")
for i in lines:
    if int(i) != 100:
        file.write(i)
file.close()
