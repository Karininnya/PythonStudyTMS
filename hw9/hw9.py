f = open('pupils.txt', 'r')
content = f.read()
f.close()
content = content.split("\n")
pupils = []
for line in content:
    line = line.split(" ")
pupils.append([line[0], line[1], int(line[2])])
srednya = 0
print("Ниже 3 баллов:")
for p in pupils:
        srednya += int(p[2])
if p[2] < 3:
 print(f"{p[0]} {p[1]}: {p[2]}")
