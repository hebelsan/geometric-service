import pytest

from shapes.plane import Plane
from shapes.polygon import Polygon


def test_polygon_is_convex():
    vertices = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    polygon = Polygon(vertices)
    assert polygon.is_convex() is True

    vertices = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0.5, 0.5, 0.5)]
    polygon = Polygon(vertices)
    assert polygon.is_convex() is False

    vertices = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (2, 1, 0)]
    polygon = Polygon(vertices)
    assert polygon.is_convex() is True

    vertices = [(0, 0, 0), (0, 1, 0), (0.5, 0.5, 0), (1, 1, 0), (1, 0, 0)]
    polygon = Polygon(vertices)
    assert polygon.is_convex() is False


def test_polygon_is_in_xy_plane():
    vertices = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    polygon = Polygon(vertices)
    assert polygon.is_in_xy_plane() is True

    vertices = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0.5, 0.5, 0.5)]
    polygon = Polygon(vertices)
    assert polygon.is_in_xy_plane() is False


def test_polygon_cut():
    vertices = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    polygon = Polygon(vertices)

    # vertical plane on x = 0.5
    point = (0.5, 0, 0)
    normal = (1, 0, 0)
    plane = Plane(point, normal)
    cut = polygon.cut(plane)
    assert (cut.vertices == [[0.5, 0, 0], [0.5, 1, 0]]).all()

    # horizontal plane on y = 0.5
    point = (0, 0.5, 0)
    normal = (0, 1, 0)
    plane = Plane(point, normal)
    cut = polygon.cut(plane)
    print(cut.vertices)
    assert (cut.vertices == [[1, 0.5, 0], [0, 0.5, 0]]).all()

    # horizontal plane on y = 2 (above polygon)
    with pytest.raises(ValueError) as err:
        point = (0, 2, 0)
        normal = (0, 1, 0)
        plane = Plane(point, normal)
        polygon.cut(plane)
    assert err.value.args[0] == 'Polygon lays outside the plane'

    # horizontal plane on y = 2 (above polygon)
    with pytest.raises(ValueError) as err:
        point = (1, 1, 0)
        normal = (0, 0, 1)
        plane = Plane(point, normal)
        polygon.cut(plane)
    assert err.value.args[0] == 'Polygon lays in plane'
