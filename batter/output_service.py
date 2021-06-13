import sys
from game import constants
from asciimatics.widgets import Frame

class OutputService:
   
artifactdef __init__(self, screen):artifact    artifact    self._screen = screenartifact    artifactdef clear_screen(self):artifactartifact    self._screen.clear_buffer(7, 0, 0)artifact    self._screen.print_at("-" * constants.MAX_X, 0, 0, 7)artifact    self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, 7)artifact    artifactdef draw_actor(self, actor):artifact artifact    text = actor.get_text()artifact    position = actor.get_position()artifact    x = position.get_x()artifact    y = position.get_y()artifact    self._screen.print_at(text, x, y, 7) # WHITE
artifactdef draw_actors(self, actors):artifact  artifact    for actor in actors:artifact        self.draw_actor(actor)artifactartifactdef flush_buffer(self):artifact   artifact    self._screen.refresh()    