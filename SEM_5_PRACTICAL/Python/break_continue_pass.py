# break – stop loop at user-specified number
stop_num = int(input("Enter a number to break the loop: "))
for i in range(1, 11):
    if i == stop_num:
        print("Breaking at", i)
        break
    print(i)

# continue – skip a number specified by user
skip_num = int(input("Enter a number to skip (continue): "))
for i in range(1, 6):
    if i == skip_num:
        continue
    print(i)

# pass – demonstrate pass inside if block
for i in range(3):
    if i == 1:
        pass
    print("Current value:", i)
