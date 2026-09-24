#5.
kirill, arina, sergey = map(int, input().split())
best = kirill
if arina > best:
    best = arina

if sergey > best:
    best = sergey

print(best)