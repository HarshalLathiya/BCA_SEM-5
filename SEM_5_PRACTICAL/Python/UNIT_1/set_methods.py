# Program: 22

cars = {"BMW", "Audi", "Tesla"}

cars.add("Toyota")
print("After add:", cars)

cars.update(["Honda", "Kia"])
print("After update:", cars)

copy_cars = cars.copy()
print("Copied set:", copy_cars)

cars.pop()
print("After pop:", cars)

cars.remove("Kia")
print("After remove:", cars)

cars.discard("Ferrari")
print("After discard:", cars)

cars.clear()
print("After clear:", cars)

a = {"Toyota", "Honda"}
b = {"Ford", "Honda"}
print("Union:", a.union(b))

print("Intersection:", a.intersection(b))

print("Difference:", a.difference(b))
