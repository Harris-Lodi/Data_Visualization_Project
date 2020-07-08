import matplotlib.pyplot as plt 

# data set of 1000 dots too look like a line
x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values] # for loop result is assigned to y_values

plt.style.use('seaborn')

fig, ax = plt.subplots()

# x values, y values, size of dots, change colors too using color map
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s = 10)

# set chart title and labels
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Input Values", fontsize=14)
ax.set_ylabel("Square of Values", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# set the range for each axis
ax.axis([0, 1100, 0, 1100000])

# save plots automatically, use plot.show() to show plot instead
plt.savefig('squares_plot.png', bbox_inches = 'tight')