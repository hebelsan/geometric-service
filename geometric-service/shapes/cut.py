import numpy as np

from flask import jsonify
from .utils import validate_vertices


class Cut:
    def __init__(self, vertices):
        self.vertices = vertices

    def serialize(self):
        return jsonify({'cut': self.vertices.tolist()})

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        validate_vertices(vertices, 2)
        self._vertices = np.array(vertices).astype(float)
