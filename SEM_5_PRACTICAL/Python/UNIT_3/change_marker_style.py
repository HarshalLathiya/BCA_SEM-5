import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 10)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot with different marker styles
plt.plot(x, y1, color="blue", marker='o', linestyle='-', label="Sine (Circle Marker)")   # Circle
plt.plot(x, y2, color="red", marker='s', linestyle='--', label="Cosine (Square Marker)") # Square

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Changing Marker Styles in Matplotlib")
plt.legend()
plt.show()