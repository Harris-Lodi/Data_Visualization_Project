from plotly.graph_objs import Bar, Layout
from plotly import offline 
from die import Die

# create one 6-sided die and one 10 sides die this time
die_1 = Die()
die_2 = Die(10)

# make some rolls, and store results in a list, page 334
results = []
for roll_num in range(50000): # 50,000 rolls

    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze the results
frequencies = []
max_results = die_1.num_sides + die_2.num_sides # add up the sides of both dies
for value in range(2, max_results+1): # start from 2 since that is the smallest sum of both sides

    # count unique value from results
    # and store the number of unique occurences in frequency
    # and them append that to frequencies
    frequency = results.count(value) 
    frequencies.append(frequency)

# visualize the results
x_values = list(range(2, max_results+1)) # x_values is die sides from 1-6, for two die it's form 2-12
data = [Bar(x = x_values, y = frequencies)] # set data axis for bar graph

# label axis, graph with appropriate titles
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title = 'Results of Rolling one D6 and one D10 die 50,000 times', xaxis = x_axis_config, yaxis = y_axis_config)

# send data to plot matrix to generate plot in an HTML file
offline.plot({'data': data, 'layout': my_layout}, filename = 'D6_D10.html')

print(frequencies)