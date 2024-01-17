import math

class CartesianPlane:
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        point = (x, y)
        self.points.append(point)

    def shortest_edge(self, point1, point2):
        if len(self.points) < 2:
            return None  # Return null if there is only one point

        if point1 not in self.points or point2 not in self.points:
            return None  # Return null if any point is not in the plane

        # Calculate Euclidean distance between two points
        distance = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

        return distance

# Example Usage:
cartesian_plane = CartesianPlane()
cartesian_plane.add_point(1, 2)
cartesian_plane.add_point(3, 4)

point1 = (1, 2)
point2 = (3, 4)

shortest_edge = cartesian_plane.shortest_edge(point1, point2)

if shortest_edge is not None:
    print(f"The shortest edge between {point1} and {point2} is {shortest_edge}")
else:
    print("There is only one point or one of the specified points is not in the plane.")
