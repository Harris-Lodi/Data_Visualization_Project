import matplotlib.pyplot as plt

# data to visualize
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# set style for the plot
plt.style.use('seaborn')

# assign fig and ax as asix for the plot
fig, ax = plt.subplots()

# plot the data to visualize, line width change to alter looks
ax.plot(input_values, squares, linewidth = 3)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Input Values", fontsize=14)
ax.set_ylabel("square of Value", fontsize=14)

# set size of tick labels
ax.tick_params(axis = 'both', labelsize = 14)

# show plot
plt.show()