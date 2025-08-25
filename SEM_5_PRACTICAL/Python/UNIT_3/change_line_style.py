import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot with different line styles
plt.plot(x, y1, color="blue", linestyle='-', label="Sine (Solid Line)")   # Solid line
plt.plot(x, y2, color="red", linestyle='--', label="Cosine (Dashed Line)") # Dashed line

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Changing Line Styles in PyLab/Matplotlib")
plt.legend()
plt.show()
