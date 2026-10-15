#6.
file = open("input.txt", "r", encoding="utf-8")
result = open("output.txt", "w", encoding="utf-8")
try:
    n = int(file.readline())
    lines = file.readlines()

    if len(lines) == n:
        result.write("YES")
    else:
        result.write("NO")

except ValueError:
    result.write("ERROR")
file.close()
result.close()
