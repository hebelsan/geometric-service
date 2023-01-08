import numpy as np
import os

from .plane import Plane
from .cut import Cut
from .utils import validate_vertices


class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    def cut(self, plane: Plane) -> Cut:
        """
        Cut the polygon at the given plane and return the resulting cut.
        
        Args:
            plane (Plane): The plane to cut the polygon at.
        
        Returns:
            Polygon: The resulting polygon after cutting.
        """
        if os.getenv('ALPHA') == 'true' and (not self.is_in_xy_plane() or not self.is_convex()):
            raise ValueError("in alpha version polygon must be in xy plane and be convex")

        if plane.is_xy_plane():
            raise ValueError("Polygon lays in plane")

        n = len(self.vertices)
        # The cut polygon will be stored in this list of points
        intersections = []

        # Iterate over the edges of the polygon
        for i in range(n):
            # Get the current vertex and the next vertex
            vertex1 = self.vertices[i]
            vertex2 = self.vertices[(i + 1) % n]

            # Check if the vertices are on opposite sides of the plane
            side1 = plane.is_above(vertex1)
            side2 = plane.is_above(vertex2)

            if side1 and not side2:
                # The edge intersects the plane and the cut point is added to the cut polygon
                intersections.append(plane.intersection(vertex1, vertex2))
            elif not side1 and side2:
                # The edge intersects the plane and the cut point is added to the cut polygon
                intersections.append(plane.intersection(vertex1, vertex2))

        if len(intersections) == 0:
            raise ValueError("Polygon lays outside the plane")

        return Cut(intersections)

    def is_in_xy_plane(self):
        """
        Check if the polygon is defined in the XY plane.
        
        Returns:
            bool: True if the polygon is defined in the XY plane, False otherwise.
        """
        for vertex in self.vertices:
            if vertex[2] != 0:
                return False
        return True

    def is_convex(self):
        """
        Check if the polygon is convex.
        In a convex polygon, all interior angles are less than or equal to 180 degrees
        
        Returns:
            bool: True if the polygon is convex, False otherwise.
        """
        n = len(self.vertices)

        # Check the direction of the cross product between consecutive edges
        prev = np.cross(self.vertices[1] - self.vertices[0], self.vertices[2] - self.vertices[1])
        for i in range(1, n):
            curr = np.cross(self.vertices[(i + 1) % n] - self.vertices[i],
                            self.vertices[(i + 2) % n] - self.vertices[(i + 1) % n])
            if np.dot(prev, curr) < 0:
                return False
            prev = curr

        return True

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        validate_vertices(vertices, 3)
        self._vertices = np.array(vertices).astype(float)
