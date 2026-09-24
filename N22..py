N, K, M = map(int, input().split())

rides = N * 2  # всего катаний
if rides % K == 0:
    sessions = rides // K
else:
    sessions = rides // K + 1
print(sessions * M)