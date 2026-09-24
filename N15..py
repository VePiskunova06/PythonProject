#15.
N, K, M = map(int, input().split())
forward = abs(M - K)

backward = N - forward
print(min(forward, backward))
