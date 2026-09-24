#19.
N, M = map(int, input().split("x"))
K = int(input())

if K % N == 0 or K % M == 0:
    print("успешно")
else:
    print("неосуществимо")