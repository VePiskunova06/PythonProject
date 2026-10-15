#4.
file = open("input.txt", "r", encoding="utf-8")
result = open("output.txt", "w", encoding="utf-8")
for line in file:
    if len(line.rstrip("\n")) > 20:
        result.write(line)

file.close()
result.close()
