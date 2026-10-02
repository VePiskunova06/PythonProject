#15.
n = int(input())

for number in range(2, n + 1):
    prime = True

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            prime = False
            break
    if prime:
        print(number)
