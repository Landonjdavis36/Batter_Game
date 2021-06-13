class Action:artifact"""A code template for a thing done in a game. The responsibility of artifactthis class of objects is to interact with actors to change the state of the game. artifactartifactStereotype:artifact    Controller
artifactAttributes:artifact    _tag (string): The action tag (input, update or output).artifact"""
artifactdef execute(self, cast):artifact    """Executes the action using the given actors.
artifact    Args:artifact        cast (dict): The game actors {key: tag, value: list}.artifact    """artifact    raise NotImplementedError("execute not implemented in superclass")