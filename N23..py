n = int(input())

hours = n // 3600
rest = n % 3600 #остаток

minutes = rest // 60
seconds = rest % 60

print(hours, "часов", minutes, "минут", seconds, "секунд")