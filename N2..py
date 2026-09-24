#2.
name = input("Имя персонажа: ")
name = name.lower()
answers = ["джеймс бонд", "007", "агент 007"]
if name in answers:
    print("верно")
else:
    print("неверно")