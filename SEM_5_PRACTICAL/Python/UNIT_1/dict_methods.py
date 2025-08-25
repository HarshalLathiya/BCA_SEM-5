# Program: 24

langs = dict(python="Easy", java="Medium", cpp="Hard")
print("Original dict:", langs)

print("Length:", len(langs))

temp = langs.copy()
temp.clear()
print("After clear():", temp)

print("Get value of 'java':", langs.get("java"))

langs.pop("cpp")
print("After pop('cpp'):", langs)

langs.popitem()
print("After popitem():", langs)

print("Keys:", langs.keys())

print("Values:", langs.values())

print("Items:", langs.items())

copy_langs = langs.copy()
print("Copied dict:", copy_langs)

copy_langs.update({"go": "Simple"})
print("After update:", copy_langs)
