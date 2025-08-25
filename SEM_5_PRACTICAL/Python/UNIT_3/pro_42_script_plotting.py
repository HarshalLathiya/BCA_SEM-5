import matplotlib.pyplot as plt
import numpy as np

# Generate values for x-axis
x = np.linspace(-10, 10, 100)   # 100 points from -10 to 10
y = x**2                        # Curve: y = x^2

# Plotting the curve
plt.plot(x, y, label="y = x²", color="blue", linewidth=2)

# Adding title and labels
plt.title("Curve Plotting Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show grid and legend
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
