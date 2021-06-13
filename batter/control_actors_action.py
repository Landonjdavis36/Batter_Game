from game import constants
from game.action import Action

class ControlActorsAction(Action):artifact"""A code template for controlling actors. The responsibility of thisartifactclass of objects is translate user input into some kind of intent.artifactartifactStereotype:artifact    Controller
artifactAttributes:artifact    _input_service (InputService): An instance of InputService.artifact"""
artifactdef __init__(self, input_service):artifact    """The class constructor.artifact    artifact    Args:artifact        input_service (InputService): An instance of InputService.artifact    """artifact    self._input_service = input_service
artifactdef execute(self, cast):artifact    """Executes the action using the given actors.
artifact    Args:artifact        cast (dict): The game actors {key: tag, value: list}.artifact    """artifact    direction = self._input_service.get_direction()artifact    robot = cast["robot"][0] # there's only one in the castartifact    robot.set_velocity(direction)        
