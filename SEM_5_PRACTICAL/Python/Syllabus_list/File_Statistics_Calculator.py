f = open("sample.txt", "w")
f.write("Harshal.\nLathiya\nBCA!")
f.close()

f = open("sample.txt", "r")

char_count = 0
word_count = 0
line_count = 0

for line in f:
    line_count += 1
    char_count += len(line)
    word_count += len(line.split())

f.close()

print("Total Lines:", line_count)
print("Total Words:", word_count)
print("Total Characters:", char_count)
