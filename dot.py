import random
import statistics
import math


# distance between points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


class Dot:
    def __init__(self, resolution):
        self.coordinates = (random.randrange(15, resolution[0]-15), random.randrange(115, resolution[1]-15))

        # resolution of surface
        self.resolution = resolution

        # distance task
        self.task = random.randrange(30, int(self.distance_to_farthest_corner()) - 100)

    # look for distance to farthest corner
    def distance_to_farthest_corner(self):
        if self.coordinates[0] <= self.resolution[0]/2 and self.coordinates[1] <= self.resolution[1]/2:
            # bottom right corner
            return distance(self.coordinates, (self.resolution[0], self.resolution[1]+50))
        elif self.coordinates[0] <= self.resolution[0]/2 and self.coordinates[1] >= self.resolution[1]/2:
            # upper right corner
            return distance(self.coordinates, (self.resolution[0], 50))
        elif self.coordinates[0] >= self.resolution[0]/2 and self.coordinates[1] <= self.resolution[1]/2:
            # bottom left corner
            return distance(self.coordinates, (0, self.resolution[1]+50))
        else:
            # upper left corner
            return distance(self.coordinates, (0, 50))

    def add_points(self, click_point):
        # distance between our Dot object (self) and clicked point in game (click_point)
        distance_self_click = distance(self.coordinates, click_point)

        pixel_point = 100000/self.distance_to_farthest_corner()

        # right_distance
        if distance_self_click < self.task:
            right_distance = self.task - distance_self_click
        else:
            right_distance = distance_self_click - self.task

        # calc points
        points = round(100000-(pixel_point*right_distance)*3)
        if points < 0:
            points = 0

        # change statistics
        statistics.points += points
        statistics.round_of_game += 1

        return points

    def __del__(self):
        pass

