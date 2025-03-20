import math
import numpy as np
import matplotlib.pyplot as plt

initialVelocity = float(input("Enter the initial velocity in m/s^2: "))
launchAngle = np.radians(float(input("Enter launch angle in degrees: ")))
gravity = float(input("Enter the acceleration due to gravity: "))

horizontal = initialVelocity * math.cos(launchAngle)
vertical = initialVelocity * math.sin(launchAngle)

timeOfFlight = (2 * vertical) / gravity

t = np.linspace(0, timeOfFlight, 100)

horizontalFunc = horizontal * t
verticalFunc = vertical * t - 0.5 * gravity * t**2

fig, ax = plt.subplots()

ax.plot(horizontalFunc, verticalFunc, color="blue")

plt.xlabel(xlabel="Distance", color="red", fontweight="bold")
plt.ylabel(ylabel="Height", color="red", fontweight="bold")
plt.ylim(bottom=0)
plt.grid()
plt.show()
