import pylab as plt

data = [10, 20, 20, 30, 30, 30, 40, 50, 50, 60, 70, 80, 90, 100]

plt.hist(data, bins=6, color='green', edgecolor='black')
plt.xlabel("Value Ranges")
plt.ylabel("Frequency")
plt.title("Histogram Example")
plt.show()
