#16.
pin = input()
if len(pin) != 4:
    print("ERROR")

elif pin[0] == pin[1] or pin[0] == pin[2] or pin[0] == pin[3]  or pin[1] == pin[2] \
        or pin[1] == pin[3] or pin[2] == pin[3]:
    print("ERROR")

elif 1900 <= int(pin) <= 2050:
    print("ERROR")

else:
    print("OK")