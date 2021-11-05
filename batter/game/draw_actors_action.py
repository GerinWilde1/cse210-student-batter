
from game.action import Action

# TODO: Define the DrawActorsAction class here
class DrawActorsAction(Action):
    def __init__(self, output_service):
        self._output_service = output_service


    def execute(self, cast):
        paddle = cast["paddle"]
        brick = cast["brick"] 
        wall = cast["wall"]
        ball = cast["ball"][0] # there's only one

        self._output_service.clear_screen()
        self._output_service.draw_actors(wall, 7)
        self._output_service.draw_actors(paddle)
        self._output_service.draw_actors(brick)
        self._output_service.draw_actor(ball, 4)

        self._output_service.flush_buffer()