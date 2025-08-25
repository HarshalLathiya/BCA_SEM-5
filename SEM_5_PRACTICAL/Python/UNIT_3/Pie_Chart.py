import pylab as plt

sizes = [30, 25, 20, 25]
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
colors = ['red', 'yellow', 'pink', 'brown']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title("Pie Chart Example")
plt.show()
