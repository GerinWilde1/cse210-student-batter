from game.action import Action
from game import actor

class DrawActorsAction(Action):
    """A code template for Draw Actors Action. 
    The responsibility of this class of objects is to draw the the actor action based on the input.
    
    Stereotype:
        Information Holder, Controller
    """

    def __init__(self, output_service):

        self._output_service = output_service


    def execute(self, cast):

        # Clear the screen
        self._output_service.clear_screen()

        # Draw actor
        for group in cast.values():
            self._output_service.draw_actors(group)

        # Flush the Buffer
        self._output_service.flush_buffer()