class Point:artifact"""Represents distance from an origin (0, 0).
artifactStereotype:artifact    Information Holder
artifactAttributes:artifact    _x (integer): The horizontal distance.artifact    _y (Point): The vertical distance.artifact"""artifactartifactdef __init__(self, x, y):artifact    """The class constructor.artifact    artifact    Args:artifact        x (integer): A horizontal distance.artifact        y (integer): A vertical distance.artifact    """artifact    self._x = xartifact    self._y = y
artifactdef add(self, other):artifact    """Gets a new point that is the sum of this and the given one.
artifact    Args:artifact        other (Point): The Point to add.
artifact    Returns:artifact        Point: A new Point that is the sum.artifact    """artifact    x = self._x + other.get_x()artifact    y = self._y + other.get_y()artifact    return Point(x, y)
artifactdef equals(self, other):artifact    """Whether or not this Point is equal to the given one.
artifact    Args:artifact        other (Point): The Point to compare.
artifact    Returns: artifact        boolean: True if both x and y are equal; false if otherwise.artifact    """artifact    return self._x == other.get_x() and self._y == other.get_y()
artifactdef get_x(self):artifact    """Gets the horizontal distance.artifact    artifact    Returns:artifact        integer: The horizontal distance.artifact    """artifact    return self._x
artifactdef get_y(self):artifact    """Gets the vertical distance.artifact    artifact    Returns:artifact        integer: The vertical distance.artifact    """artifact    return self._y
artifactdef is_zero(self):artifact    """Whether or not the point is zero or x = 0 and y = 0.artifact    artifact    Returns:artifact        boolean: True if x = 0 and y = 0; false if otherwise.artifact    """artifact    return self._x == 0 and self._y == 0artifact    artifactdef reverse(self):artifact    """Gets a new Point that is the reverse of this one.artifact    artifact    Returns:artifact        Point: A new Point that is reversed.artifact    """artifact    x = self._x * -1artifact    y = self._y * -1artifact    return Point(x, y)