#16.
n = int(input())

for number in range(2, n + 1):
    sum_divisors = 0
    for divisor in range(1, number // 2 + 1):
        if number % divisor == 0:
            sum_divisors += divisor

    if sum_divisors == number:
        print(number)