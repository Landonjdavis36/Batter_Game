import random
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):artifact
artifactdef execute(self, cast):artifact    artifact brick = cast["brick"][0] # there's only oneartifact    bat = cast["bat"][0] # there's only oneartifact    artifacts = cast["artifact"]artifact    brick.set_text("")artifact    for artifact in artifacts:artifact        if bat.get_position().equals(artifact.get_position()):artifact            description = artifact.get_description()artifact           bat.set_text(description) 