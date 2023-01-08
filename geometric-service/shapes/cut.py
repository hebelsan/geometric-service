import numpy as np

from .utils import validate_vertices


class Cut:
    def __init__(self, vertices):
        self.vertices = vertices

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        validate_vertices(vertices, 2)
        self._vertices = np.array(vertices).astype(float)
