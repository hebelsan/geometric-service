import numbers


def validate_vertices(vertices, min_vertices):
    """
    Validates the format of 3D vertices, raises an Exception if not satisfied
    """
    if not isinstance(vertices, list):
        raise ValueError("Vertices must be a list of 3D points (tuples of three floats)")
    if len(vertices) < min_vertices:
        raise ValueError(f"Vertices must be a list of min {min_vertices} 3D points")
    for point in vertices:
        validate_point(point)


def validate_point(point):
    """
    Validates the format of a 3D point, , raises an Exception if not satisfied
    """
    if len(point) != 3:
        raise ValueError("Point must be a 3D vector (tuple/list of three floats)")
    for coord in point:
        if not isinstance(coord, numbers.Number):
            raise ValueError("3D Point coordinate is not of type number")
