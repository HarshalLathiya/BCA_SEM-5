import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot with different line colors
plt.plot(x, y, color='red', label="Red Line")        # Using color name
plt.plot(x, y+1, 'g', label="Green Line")            # Using short code
plt.plot(x, y+2, color='#1f77b4', label="Blue Hex")  # Using hex code

# Adding labels and legend
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Colors Example")
plt.legend()
plt.show()
