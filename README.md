# Geometric Service

This is library contains a REST API for geometric calculations (so far only polygon and plane intersection).

## Requirements
- python > 3.6
- python-venv

## Installation

To install the library, clone the repository and install the dependencies:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


## Usage

To use the library, import the `Polygon` and `Plane` classes and create instances of them:

```python
from shapes import Polygon, Plane

vertices = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
polygon = Polygon(vertices)

point = (0, 0, 0)
normal = (0, 0, 1)
plane = Plane(point, normal)

cut_polygon = polygon.cut(plane)
```

## Development

To run the tests:
TODO