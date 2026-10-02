#3.
while True:
    x = int(input())
    root = x ** 0.5
    if root == int(root):
        print("полный квадрат")
        break
    else:
        print("не квадрат")