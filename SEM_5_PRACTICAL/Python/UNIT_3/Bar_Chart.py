import pylab as plt

x = ['A', 'B', 'C', 'D']
y = [3, 7, 5, 9]

plt.bar(x, y, color='orange')
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart Example")
plt.show()
