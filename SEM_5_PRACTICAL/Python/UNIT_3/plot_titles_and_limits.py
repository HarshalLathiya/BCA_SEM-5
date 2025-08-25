import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot
plt.plot(x, y, color="blue", marker="o", linestyle="-")

# Adding title and axis labels
plt.title("Sine Wave Example")      # Plot Title
plt.xlabel("X-Axis (Time)")         # X-Axis Label
plt.ylabel("Y-Axis (Amplitude)")    # Y-Axis Label

# Setting axis limits
plt.xlim(0, 12)   # Limit for X-axis
plt.ylim(-2, 2)   # Limit for Y-axis

plt.show()
