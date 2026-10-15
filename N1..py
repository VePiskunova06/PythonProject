#1.
file = open("input.txt", "r", encoding="utf-8")
text = file.read()
file.close()

text = text.upper()
file = open("output.txt", "w", encoding="utf-8")
file.write(text)
file.close()
