#8.
playlist = []
print("Введите плей-лист папы:")
for i in range(5):
    song = input()
    playlist.append(song)
print("Плей-лист мамы:")

for song in reversed(playlist):
    print(song)