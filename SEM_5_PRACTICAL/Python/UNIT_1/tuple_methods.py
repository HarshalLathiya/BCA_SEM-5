# Program: 20

t = (5, 2, 8, 2, 1)

print("Length:", len(t))
print("Count of 2:", t.count(2))
print("Index of 8:", t.index(8))
print("Sorted tuple (as list):", sorted(t))
print("Minimum:", min(t))
print("Maximum:", max(t))

# vii) Simulating cmp() for comparing two tuples
t1 = (1, 2, 3)
t2 = (1, 2, 4)

if t1 == t2:
    print("cmp(t1, t2): 0 (Equal)")
elif t1 < t2:
    print("cmp(t1, t2): -1 (t1 < t2)")
else:
    print("cmp(t1, t2): 1 (t1 > t2)")

print("Reversed tuple:", tuple(reversed(t)))
