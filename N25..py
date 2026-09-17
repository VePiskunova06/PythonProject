x, y, n = map(int, input().split())#рубли, копейки, количество

total = (x * 100 + y) * n
print(total // 100, "руб.", total % 100, "коп.")