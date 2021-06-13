import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 

def main(screen):
artifact# create the cast {key: tag, value: list}artifactcast = {}
artifactx = int(constants.MAX_X / 2)artifacty = int(constants.MAX_Y - 1)artifactposition = Point(x, y)artifactpaddle = Actor()artifactpaddle.set_text("===========")artifactpaddle.set_position(position)artifactcast["paddle"] = [paddle]
artifactcast["brick"] = []artifactfor x in range(5, 75):artifact    for y in range(2, 6):artifact        position = Point(x, y)artifact        brick = Actor()artifact        brick.set_text("*")artifact        brick.set_position(position)artifact        cast["brick"].append(brick)
artifactx = int(constants.MAX_X / 2)artifacty = int(constants.MAX_Y / 2)artifactposition = Point(x, y)artifactvelocity = Point(1, -1)artifactball = Actor()artifactball.set_text("@")artifactball.set_position(position)artifactball.set_velocity(velocity)artifactcast["ball"] = [ball]artifactartifact# create the script {key: tag, value: list}artifactscript = {}
artifactinput_service = InputService(screen)artifactoutput_service = OutputService(screen)artifactcontrol_actors_action = ControlActorsAction(input_service)artifactmove_actors_action = MoveActorsAction()artifacthandle_collisions_acition = HandleCollisionsAction()artifactdraw_actors_action = DrawActorsAction(output_service)artifactartifactscript["input"] = [control_actors_action]artifactscript["update"] = [move_actors_action, handle_collisions_acition]artifactscript["output"] = [draw_actors_action]
artifact# start the gameartifactdirector = Director(cast, script)artifactdirector.start_game()

Screen.wrapper(main)