"""goldhunt

This module contais the code for the 'Gold Hunt' scenario set up to understand
different ways to approach a performance problem and how to optimze it.

This module is written with Python 3.8.x
"""
import sys
import time
import numpy as np

if sys.version_info < (3, 0):
    print("This code requires Python 3.x.")
    print("Looks like you are trying to run this using Python version: "
          " {0}.{1}".format(sys.version_info[0], sys.version_info[1]))
    print("Exiting...")
    sys.exit(1)

try:
    import matplotlib.pyplot as plt
except ImportError:
    msg = "You won't be able to visualize the random point distribution."
    print("ImportError: matplotlib.pyplot")
    print(msg)

def plot_points(ref_radius, x_coords, y_coords):
    """Utility function to show the 'Gold Field'!"""
    # Define axis limits
    a1 = ref_radius + 1
    a2 = a1*(-1.0)
    plt.plot(x_coords, y_coords, ".", color="#A67C00", ms=4)
    plt.axis([a2, a1, a2, a1])
    plt.show()

# Enable the @profile decorator only when you are running line_profiles or
# memory_profiler. Otherwise it will throw an error.
#@profile
def generate_random_points(ref_radius, total_points, show_plot):
    """Return x, y coordinate lists representing random points inside a circle.

    Generates random points inside a circle with center at (0,0). For any point
    it randomly picks a radius between 0 and ref_radius.

    The run time performance of this function will be significantly faster
    compared to the previous optimization pass.

    :param ref_radius: the random point lies between 0 and this radius.
    :param total_points: total number of random points to be created
    :param show_plot: boolean value to show the distribution of points.

    :return: x and y coordinates as numpy arrays
    """
    # Combination of "avoiding the dots" (function reevaluations) and
    # using local variables. It also uses the numpy library
    l_uniform = np.random.uniform
    l_sqrt = np.sqrt
    l_pi = np.pi
    l_cos = np.cos
    l_sin = np.sin

    # Note that the variables theta and radius are now numpy arrays
    theta = l_uniform(0.0, 2.0 * l_pi, total_points)
    radius = ref_radius * l_sqrt(l_uniform(0.0, 1.0, total_points))
    x = radius * l_cos(theta)
    y = radius * l_sin(theta)

    if show_plot:
        plot_points(ref_radius, x, y)

    return x, y

class GoldHunt:
    """Class to play a game scenario 'Great Gold Hunt' in 'Attack of The Orcs'.

    This class illustrates various bottlenexk that impact the performace of the
    application. The bottleneck will be visible depending of the input arguments
    to __init__ (class initializer). For example, setting field_coins to a large
    number and/or making the search radius very small.

    A word of caution: check your memory status and usage, this may consume it
    a lot.

    :ivar int field_coins: gold coins scattered over a circular field.
    :ivar float field_radius: radius of the circular field with gold coins.
    :ivar float search radius: radius of a circle. The gold search will be
            constrained within this circle.
    :ivar float x_ref: x-coordinate of the game unit searching for gold.
    :ivar float y_ref: y-coordinate of the game unit searching for gold.
    :ivar float move_distance: distance by which the game unit advances for
            the next search.
    :ivar boolean show_plot: option that shows the coins field.
    """
    def __init__(self, field_coins=5000, field_radius=10.0, search_radius=1.0, show_plot=True):
        self.field_coins = field_coins
        self.field_radius = field_radius
        self.search_radius = search_radius
        self.show_plot = show_plot

        # Game unit's initial coordinates e.g. (-9.0, 0)
        self.x_ref = - (self.field_radius - self.search_radius)
        self.y_ref = 0.0

        # Distance by which game unit advances for the next search
        self.move_distance = 2*self.search_radius

    def reset_params(self):
        """Resets some dependent params to their default computed value."""
        self.x_ref = - (self.field_radius - self.search_radius)
        self.move_distance = 2*self.search_radius

    #@profile
    def find_coins(self, x_list, y_list):
        """Return list of coins that lie within a given distance.

        :param x_list: list of x coordinates of all the coins (points)
        :param y_list: list of y coordinates of all the coins (points)

        :return: a list containing (x,y) coordinates of all the eligible coins
        """
        collected_coins = []

        # Compute the square of the search radius needed later
        search_radius_square = self.search_radius ** 2

        # Assign collected_coins.append to a local function
        append_coins_function = collected_coins.append

        # Create a single 'points' array from (x_list, y_list)
        # representing x, y coordinates.
        points = np.dstack((x_list, y_list))

        # Array representing the center of search circle
        center = np.array([self.x_ref, self.y_ref])
        diff = points - center

        # Use einsum to get array representing distance squares
        distance_squares = np.einsum('...i,...i', diff, diff)

        # Convert it to Python list (list of 'distance squares')
        dist_sq_list = distance_squares[0].tolist()

        for i, d in enumerate(dist_sq_list):

            # i is the index, d is the value of the list item
            if d <= search_radius_square:

                # See the definition of append_coins_function before the for
                # loop. It is used in place of collected_coins.append for
                # speedup.
                append_coins_function((x_list[i], y_list[i]))

        return collected_coins

    def play(self):
        """Functions that enables to play the game"""
        total_collected_coins = []
        x_list, y_list = generate_random_points(self.field_radius,
                                                self.field_coins,
                                                self.show_plot)
        count = 0
        while self.x_ref <= 9.0:
            count += 1

            # Find all the coins that lie within the circle of radius 1 unit
            coins = self.find_coins(x_list, y_list)
            print("Circle# {num}, center: ({x}, {y}), coins: {gold}".format(
                num=count, x=self.x_ref, y=self.y_ref, gold=len(coins)))

            # Update the main list that keeps record of all collected coins.
            total_collected_coins.extend(coins)

            # Move to the next position along positive X axis
            self.x_ref += self.move_distance

        print("Total collected coins: {0}".format(len(total_collected_coins)))

if __name__ == '__main__':
    start = time.perf_counter()
    game = GoldHunt(show_plot=False)
    game.play()
    end = time.perf_counter()
    print("Total time delta (time interval): {0}".format(end - start))
