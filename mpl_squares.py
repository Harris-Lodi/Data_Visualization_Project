import matplotlib.pyplot as plt

# data to visualize
squares = [1,4,9,16,25]

# assign fig and ax as asix for the plot
fig, ax = plt.subplots()

# plot the data to visualize
ax.plot(squares)

# show plot
plt.show()