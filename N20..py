cell = input()
letter = cell[0]
number = int(cell[1])

if letter in "aceg":
    if number % 2 == 1:
        print("черный")
    else:
        print("белый")
else:
    if number % 2 == 0:
        print("черный")
    else:
        print("белый")