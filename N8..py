#8.
n = int(input())
variants = 1
questions = 0

while variants < n:
    variants *= 2
    questions += 1
print(questions)