from game import constants
from game.action import Action
from game.point import Point

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction()
        paddlePart = cast["paddle"]
        if not(paddlePart[0].get_position().get_x() == 1) and\
            not(paddlePart[10].get_position().get_x() == constants.MAX_X-1):
            for paddleParts in paddlePart:
                paddleParts.set_velocity(direction)
        elif paddlePart[0].get_position().get_x() == 1 and direction.get_x() > 0:
            for paddleParts in paddlePart:
                paddleParts.set_velocity(direction)
        elif paddlePart[10].get_position().get_x() == constants.MAX_X-1 and direction.get_x() < 0:
            for paddleParts in paddlePart:
                paddleParts.set_velocity(direction) 
        else:
            for paddleParts in paddlePart:
                paddleParts.set_velocity(Point(0,0))