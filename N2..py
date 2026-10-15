#2.
file = open("input.txt", "r", encoding="utf-8")
result = open("output.txt", "w", encoding="utf-8")
for i in file:
    if i[0] == "A" or i[0] == "a":
        result.write(i)

file.close()
result.close()
