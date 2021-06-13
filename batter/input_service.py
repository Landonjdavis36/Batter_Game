import sys
from game.point import Point
from asciimatics.event import KeyboardEvent

class InputService:artifact"""Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.
artifactStereotype: artifact    Service Provider
artifactAttributes:artifact    _screen (Screen): An Asciimatics screen.artifact    _keys (list): Points for up, dn, lt, rt.artifact"""
artifactdef __init__(self, screen):artifact    """The class constructor."""artifact    self._screen = screenartifact    self._keys = {}artifact    self._keys[119] = Point(0, -1) # wartifact    self._keys[115] = Point(0, 1) # sartifact    self._keys[97] = Point(-1, 0) # aartifact    self._keys[100] = Point(1, 0) # dartifact    artifactdef get_direction(self):artifact    """Gets the selected direction for the given player.
artifact    Returns:artifact        Point: The selected direction.artifact    """artifact    direction = Point(0, 0)artifact    event = self._screen.get_event()artifact    if isinstance(event, KeyboardEvent):artifact        if event.key_code == 27:artifact            sys.exit()artifact        direction = self._keys.get(event.key_code, Point(0, 0))artifact    return direction