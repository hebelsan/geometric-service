import numpy as np
import numbers

from .utils import validate_point


class Plane:
    def __init__(self, point, normal):
        self.point = point
        self.normal = normal

    def is_inside(self, point):
        # Calculate the distance from the point to the plane
        d = np.dot(self.normal, (point - self.point))
        return d == 0

    def is_above(self, point):
        # Calculate the distance from the point to the plane
        d = np.dot(self.normal, (point - self.point))
        # If the distance is positive, the point is above the plane
        if d > 0:
            return True
        else:
            return False

    def is_xy_plane(self):
        # Check if the normal vector is [0, 0, 1] or [-0, -0, -1]
        return np.array_equal(self.normal, [0, 0, 1]) or np.array_equal(self.normal, [-0, -0, -1])

    def intersection(self, point1, point2):
        # Calculate the distance from the points to the plane
        d1 = np.dot(self.normal, (point1 - self.point))
        d2 = np.dot(self.normal, (point2 - self.point))

        # Calculate the intersection point
        intersection_point = point1 - d1 / (d1 - d2) * (point1 - point2)

        return intersection_point

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, point):
        validate_point(point)
        self._point = np.array(point).astype(float)

    @property
    def normal(self):
        return self._normal

    @normal.setter
    def normal(self, normal):
        validate_point(normal)
        self._normal = np.array(normal).astype(float)
