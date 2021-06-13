from game import constants
from game.action import Action
from game.point import Point

class MoveActorsAction(Action):
   artifactdef execute(self, cast):artifact    artifact    for group in cast.values():artifact        for actor in group:artifact            if not actor.get_velocity().is_zero():artifact                self._move_actor(actor)
artifactdef _move_actor(self, actor):artifact artifact    position = actor.get_position()artifact    velocity = actor.get_velocity()artifact    x1 = position.get_x()artifact    y1 = position.get_y()artifact    x2 = velocity.get_x()artifact    y2 = velocity.get_y()artifact    x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)artifact    y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)artifact    position = Point(x, y)artifact    actor.set_position(position)