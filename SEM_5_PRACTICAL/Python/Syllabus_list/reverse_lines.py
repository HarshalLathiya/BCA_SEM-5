f = open("lines.txt", "w")
f.write("Harshal\nLathiya\nBCA")
f.close()

f = open("lines.txt", "r")
for line in f:
    print(line.strip()[::-1])
f.close()
