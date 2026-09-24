#18.
A, B = map(int, input().split("x"))
C, D, E = map(int, input().split("x"))
if ((C <= A and D <= B) or
    (C <= B and D <= A) or
    (C <= A and E <= B) or
    (C <= B and E <= A) or (D <= A and E <= B) or (D <= B and E <= A)):
    print("да")
else:
    print("нет")