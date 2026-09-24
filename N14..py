#14.
n = int(input())
galleon = n // (17 * 29)
n = n % (17 * 29)

sickle = n // 29
knot = n % 29

if galleon != 0:
    print(galleon, "галлеонов")

if sickle != 0:
    print(sickle, "сиклей")

if knot != 0:
    print(knot, "кнатов")