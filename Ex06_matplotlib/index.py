import matplotlib.pyplot as plt

# Define x and y data
x = [1, 2, 3, 4, 5]
y = [1, 3, 2, 4, 5]

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the data on the axis
ax.plot(x, y)

# Set the axis labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('My Line Graph')

# Show the plot
plt.show()
