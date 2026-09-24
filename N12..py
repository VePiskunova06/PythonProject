#12.
n = int(input())
if n % 10 == 1 and n % 100 != 11:
    print(n, "попугай")

elif (n % 10 == 2 or n % 10 == 3 or n % 10 == 4) and not (12 <= n % 100 <= 14):
    print(n, "попугая")

else:
    print(n, "попугаев")