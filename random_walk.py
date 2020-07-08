from random import choice

# a class to generate random walks, 
# look up random walks on google for definitions 
# and tutorials/applications
class Randomwalk:

    # init the attributes of a walk, num_points set to 5000 by default
    def __init__(self, num_points = 5000):

        self.num_points = num_points

        # all walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    # function to fill our walk with points and 
    # determine the direction of each step
    def fill_walk(self):

        # calculate all points on walk
        while len(self.x_values) < self.num_points:

            # decide which direction to go and 
            # how far in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate new positons, 
            # by adding new steps to end of x/y_values lists 
            # and saving them as x and y, and then appending
            # them to x/y_values lists
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)