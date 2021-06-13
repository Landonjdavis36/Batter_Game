from game.action import Action

class DrawActorsAction(Action):artifact"""A code template for drawing actors. The responsibility of this class ofartifactobjects is use an output service to draw all actors on the screen.artifactartifactStereotype:artifact    Controller
artifactAttributes:artifact    _output_service (OutputService): An instance of OutputService.artifact"""
artifactdef __init__(self, output_service):artifact    """The class constructor.artifact    artifact    Args:artifact        output_service (OutputService): An instance of OutputService.artifact    """artifact    self._output_service = output_service
artifactdef execute(self, cast):artifact    """Executes the action using the given actors.
artifact    Args:artifact        cast (dict): The game actors {key: tag, value: list}.artifact    """artifact    self._output_service.clear_screen()artifact    for group in cast.values():artifact        self._output_service.draw_actors(group)artifact    self._output_service.flush_buffer()
