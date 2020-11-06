import random
import math
import statistics

class Dot:
    def __init__(self, resolution):
        self.coordinates = (random.randrange(15, resolution[0]-15), random.randrange(15, resolution[1]-15))

        # resolution of surface
        self.resolution = resolution

        # distance task
        self.task = random.randrange(30, int(self.distance_to_farthest_corner()))

    # distance between points
    def distance(self, point1, point2):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    # look for distance to farthest corner
    def distance_to_farthest_corner(self):
        if self.coordinates[0] <= self.resolution[0]/2 and self.coordinates[1] <= self.resolution[1]/2:
            # bottom right corner
            return self.distance(self.coordinates, self.resolution)
        elif self.coordinates[0] <= self.resolution[0]/2 and self.coordinates[1] >= self.resolution[1]/2:
            # upper right corner
            return self.distance(self.coordinates, (self.resolution[0], 0))
        elif self.coordinates[0] >= self.resolution[0]/2 and self.coordinates[1] <= self.resolution[1]/2:
            # bottom left corner
            return self.distance(self.coordinates, (0, self.resolution[0]))
        else:
            # upper left corner
            return self.distance(self.coordinates, (0, 0))

    def add_points(self, click_point, radius):
        # distance between our Dot object (self) and clicked point in game (click_point)
        distance_self_click = self.distance(self.coordinates, click_point)

        pixel_point = 100000/self.distance_to_farthest_corner()

        # right_distance
        if distance_self_click < radius:
            right_distance = radius - distance_self_click
        else:
            right_distance = distance_self_click - radius

        # calc points
        points = round(100000-(pixel_point*right_distance)*3)
        if points < 0:
            points = 0

        # change statistics
        statistics.points += points
        statistics.round_of_game += 1

        return points

