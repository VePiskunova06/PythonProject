#9.
import os
os.makedirs("simple", exist_ok=True)

file = open("input.txt", "r", encoding="utf-8")
result = open("simple/output.txt", "w", encoding="utf-8")

n = 0
for line in file:
    n += 1
    if n % 2 == 0:
        result.write(line)
file.close()
result.close()
