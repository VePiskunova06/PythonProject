#3.
file = open("input.txt", "r", encoding="utf-8")
result = open("output.txt", "w", encoding="utf-8")
for line in file:
    if line.strip():
        result.write(line[0])

file.close()
result.close()
