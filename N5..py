#5.
file = open("input.txt", "r", encoding="utf-8")
result = open("output.txt", "w", encoding="utf-8")

try:
    a = int(file.readline())
    b = int(file.readline())
    c = int(file.readline())

    answer = a / b + c
    result.write(str(answer))

except ValueError:
    result.write("data error")
except ZeroDivisionError:
    result.write("division by 0")
file.close()
result.close()
