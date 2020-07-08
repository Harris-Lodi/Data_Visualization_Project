import matplotlib.pyplot as plt 
from random_walk import Randomwalk

# this script will visually plot the randomwalks
# generated from the random_walk.py script, page 324

# keep making new walks, as long as the program is active
while True:
    # make random walk
    rw = Randomwalk(50000) # changed the num_points from default
    rw.fill_walk()

    # plot the points in the walk
    plt.style.use('classic') 
    # to set it to system resolution: plt.subplots(figsize=(10, 6), dpi=128)
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128) # set plot aspect ratio and size
    # color the points
    point_numbers = range(rw.num_points)
    # scatter plot uses x and y values from rw, size of plot is 15, and color parameters are inserted
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)
    # emphasize the first(Big Blue) and then the last(Big Red) points
    ax.scatter(0, 0, edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # remove tha axes, comment out the following 2 lines if you want the 
    # axis back
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    # close the graph to queue the input prompt
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break # end while loop and stop program