import pylab as plt

x = [5, 7, 8, 7, 6, 9, 5, 6, 7, 8]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

plt.scatter(x, y, color='purple', marker='*')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot Example")
plt.show()
